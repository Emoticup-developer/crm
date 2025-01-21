import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from django.db.models import Count
from api.models import *
from django.utils import timezone

def chart_view():
    # List of models to process
    models = [Client, Product, Machine, Company, Location, Ticket, Order, Localization]

    model_names = []
    day_counts = []
    month_counts = []
    year_counts = []

    # Get current date, month, and year
    current_day = timezone.now().date()
    current_month = timezone.now().month
    current_year = timezone.now().year

    # Loop through models to gather counts
    for model in models:
        model_name = model.__name__
        model_names.append(model_name)

        # Day-wise data (Count records created today)
        day_count = model.objects.filter(created_at__date=current_day).count()
        day_counts.append(day_count)

        # Month-wise data (Count records created in the current month)
        month_count = model.objects.filter(created_at__year=current_year, created_at__month=current_month).count()
        month_counts.append(month_count)

        # Year-wise data (Count records created this year)
        year_count = model.objects.filter(created_at__year=current_year).count()
        year_counts.append(year_count)

    # Prepare DataFrames for easy plotting
    df_day = pd.DataFrame({'Model': model_names, 'Day Count': day_counts})
    df_month = pd.DataFrame({'Model': model_names, 'Month Count': month_counts})
    df_year = pd.DataFrame({'Model': model_names, 'Year Count': year_counts})

    # Plotting Day-wise Counts
    fig_day, ax_day = plt.subplots()
    ax_day.bar(df_day['Model'], df_day['Day Count'])
    ax_day.set_title('Day-wise Counts')
    

    fig_day.autofmt_xdate(rotation=45)

    # Save the Day chart as a PNG image
    img_day = BytesIO()
    fig_day.savefig(img_day, format='png')
    img_day.seek(0)
    day_chart_url = base64.b64encode(img_day.getvalue()).decode('utf-8')

    # Plotting Month-wise Counts
    fig_month, ax_month = plt.subplots()
    ax_month.bar(df_month['Model'], df_month['Month Count'])
    ax_month.set_title('Month-wise Counts')
   

    fig_month.autofmt_xdate(rotation=45)

    # Save the Month chart as a PNG image
    img_month = BytesIO()
    fig_month.savefig(img_month, format='png')
    img_month.seek(0)
    month_chart_url = base64.b64encode(img_month.getvalue()).decode('utf-8')

    # Plotting Year-wise Counts
    fig_year, ax_year = plt.subplots()
    ax_year.bar(df_year['Model'], df_year['Year Count'])
    ax_year.set_title('Year-wise Counts')


    fig_year.autofmt_xdate(rotation=45)

    # Save the Year chart as a PNG image
    img_year = BytesIO()
    fig_year.savefig(img_year, format='png')
    img_year.seek(0)
    year_chart_url = base64.b64encode(img_year.getvalue()).decode('utf-8')

    
    context = {}
    context["day_chart_url"] = day_chart_url
    context["month_chart_url"] = month_chart_url
    context["year_chart_url"] = year_chart_url
    # Render the HTML with the chart URLs
    
    return context
