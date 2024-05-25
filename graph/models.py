from django.db import models


class GraphData(models.Model):
    title = models.CharField(max_length=100, default="Graph")
    x_label = models.CharField(max_length=100, default="X")
    y_label = models.CharField(max_length=100, default="Y")
    x_values = models.CharField(max_length=1000)
    y_values = models.CharField(max_length=1000)
    graph_type = models.CharField(max_length=20)
    color_preference = models.CharField(max_length=50)
    grid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
