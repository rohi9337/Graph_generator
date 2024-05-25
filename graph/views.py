import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from django.conf import settings
from django.shortcuts import render, redirect
from .models import GraphData
from django.http import HttpResponse


def graph_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        x_label = request.POST['x_label']
        y_label = request.POST['y_label']
        x_values = request.POST['x_values']
        y_values = request.POST['y_values']
        color_preference = request.POST['color_preference']
        graph_type = request.POST['graph_type']
        grid = 'grid' in request.POST  # Check if the 'grid' checkbox is checked

        graph_data = GraphData(
            title=title,
            x_label=x_label,
            y_label=y_label,
            x_values=x_values,
            y_values=y_values,
            color_preference=color_preference,
            graph_type=graph_type,
            grid=grid
        )
        graph_data.save()

        return redirect('graph:graph_view', pk=graph_data.pk)

    return render(request, 'graph_form.html')


def graph_view(request, pk):
    graph_data = GraphData.objects.get(pk=pk)

    x_values = np.array([float(x) for x in graph_data.x_values.split(',')])
    y_values = np.array([float(y) for y in graph_data.y_values.split(',')])

    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

    # Create the chart
    fig, ax = plt.subplots(figsize=(8, 6))
    if graph_data.graph_type == 'line':
        ax.plot(x_values, y_values, color=graph_data.color_preference)
    elif graph_data.graph_type == 'scatter':
        ax.scatter(x_values, y_values, color=graph_data.color_preference)
    elif graph_data.graph_type == 'bar':
        ax.bar(x_values, y_values, color=graph_data.color_preference)
    elif graph_data.graph_type == 'histogram':
        ax.hist(x_values, bins=int(y_values[0]),
                color=graph_data.color_preference)
    ax.set_xlabel(graph_data.x_label, fontdict=font2)
    ax.set_ylabel(graph_data.y_label, fontdict=font2)
    ax.set_title(graph_data.title, fontdict=font1)
    if graph_data.grid:
        ax.grid(True)

    # Save the chart to a buffer
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = buffer.getvalue()
    buffer.close()

    # Encode the image to base64 for display in the template
    graph = base64.b64encode(image_data).decode('utf-8')

    context = {'graph': graph, 'graph_data': graph_data}
    return render(request, 'graph_view.html', context)


def save_graph(request, pk):
    graph_data = GraphData.objects.get(pk=pk)

    # Create the chart
    fig, ax = plt.subplots(figsize=(8, 6))
    if graph_data.graph_type == 'line':
        ax.plot(np.array([float(x) for x in graph_data.x_values.split(',')]),
                np.array([float(y) for y in graph_data.y_values.split(',')]),
                color=graph_data.color_preference)
    elif graph_data.graph_type == 'scatter':
        ax.scatter(np.array([float(x) for x in graph_data.x_values.split(',')]),
                   np.array([float(y)
                            for y in graph_data.y_values.split(',')]),
                   color=graph_data.color_preference)
    ax.set_xlabel(graph_data.x_label)
    ax.set_ylabel(graph_data.y_label)
    ax.set_title(graph_data.title)
    if graph_data.grid:
        ax.grid(True)

    # Save the chart to a file
    file_name = f'graph_{graph_data.pk}.png'
    fig.savefig(file_name, format='png')

    # Serve the file as a response
    with open(file_name, 'rb') as file:
        response = HttpResponse(file.read(), content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
