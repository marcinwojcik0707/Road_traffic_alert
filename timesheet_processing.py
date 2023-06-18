import pandas as pd
from datetime import date
import main
import google_maps
from os import environ
from dotenv import load_dotenv
def timesheet_filtering(employee_name):
    """Clean data in excel timesheet file, filter and find work shift for a given employee.
    Used pandas library.
    Args:
        employee_name (str): employee name used in timesheet file
    """    
    # Read an Excel file into a pandas DataFrame
    df = pd.read_excel('Grafik_2023.xlsx')
    # Cleaning DataFrame
    df = df.drop(index=[0], columns='Unnamed: 0')
    df = df.rename(columns={'GRAFIK':'Date','Unnamed: 2':'Day_of_the_week'})
    # Convert columne Date to a normalize format
    df['Date']=pd.to_datetime(df['Date']).dt.date
    df['Date']=pd.to_datetime(df['Date']).dt.normalize()
    # Searching for what shift the selected employee is working on today
    df=df[(df['Date']) == str(date.today())]
    df=df[employee_name]
    shift = (df.iloc[0][0])
    return shift
def schedule_checking_road_traffic(employee_name):
    """Schedule checking road traffic depending on employee shift in work.

    Args:
        employee_name (str): employee name used in timesheet file
    """    
    shift = int(timesheet_filtering(employee_name))
    load_dotenv()
    home_address = environ.get('HOME_ADDRESS')
    work_address = environ.get('WORK_ADDRESS')
    normal_time_of_travel = environ.get('NORMAL_TIME_OF_TRAVEL')
    work_time = {
        1: {'Start_work': '5:01', 'Finish_work':'13:30'},
        2: {'Start_work':'13:00', 'Finish_work':'21:30'}, 
        3: {'Start_work':'21:00', 'Finish_work':'4:55'}
        }
    if shift in work_time.keys():
        print("here")
        main.schedule.every().day.at(work_time[shift]['Start_work']).do(google_maps.route_traffic_checking, home_address, work_address, normal_time_of_travel)
        main.schedule.every().day.at(work_time[shift]['Finish_work']).do(google_maps.route_traffic_checking, work_address, home_address, normal_time_of_travel)