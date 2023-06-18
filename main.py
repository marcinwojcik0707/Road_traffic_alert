import schedule
import time
import timesheet_processing

if __name__ == '__main__':
    """Starting appication at scheduled time 
    """    
    schedule.every().day.at("19:38").do(timesheet_processing.schedule_checking_road_traffic, 'MWó')
    while True:
        schedule.run_pending()
        # print(schedule.get_jobs()) - uncomment to see actual jobs to do by scheduler
        time.sleep(1)