
## pipeline：

- Open browser: init_driver()
- Enter the URL and sign in: handle_login(driver)
- Enter the history-user record page and close the employee management page: goto_download_page(driver)
- Enter your name, click Search, extract the data from the time period, and save as csv: download(driver, name, time_end, time_start)
- Close the browser：driver.close()

Because the network speed is not good, sometimes the data will be incomplete. if not loaded, re-run or adjust WAIT_TIME.

## require:

- python3.0+
- pandas
- selenium
- chrome
- chromedriver
