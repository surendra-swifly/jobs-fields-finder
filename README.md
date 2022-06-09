### Elements that can be used as Input the file

* input
* select
* textarea
* checkbox
* radio
* file
* button 


## Feedback loop




### CHALLENGES
* Sites rendering using javascript : https://apply.workable.com/arena-flowers/j/FF3F373882/apply/
* Sites need to first sign in to see the job description and apply : 
* Some sites only sending the email address to send the CV : https://www.piemedicalimaging.com/about-jobs/c-senior-allround-developer-mv

    


### APPROACH
* crawler.py - Scraping the site and extracting the data
     - Crawles the apply pages and get to the fields | most of the time required cookies
     - Dynamic loading of the site 
        - Accept cookies  - True or False 
        - Time wait for the page to load
        - Click some Apply Button / Have multiple pages next page 
        - Captcha can be found on some of the pages
         

* checker.py -- filters the field find the required fields and try to find it's locator which we using on the apply.py for applying and 
communicate with the database to get the data
        - Some required fields are not found on the our database
        
* apply.py -- (using selenium/playwright)
