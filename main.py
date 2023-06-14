import schedule
import time
import timesheet_processing

if __name__ == '__main__':
    schedule.every().day.at("20:17").do(timesheet_processing.timesheet, 'MWó')
    while True:
        schedule.run_pending()
        print(schedule.get_jobs())
        time.sleep(1)