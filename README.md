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
* Crawler - Scraping the site and extracting the data
     - Crawles the apply pages and get to the fields | most of the time required cookies
     - Dynamic loading of the site 
        - Accept cookies  - True or False
        - Time wait for the page to load
        - Click some Apply Button / Have muliple pages next page
         

* Checker/Validator -- Checking the data and making sure it is correct
* Applyer -- (using selenium)