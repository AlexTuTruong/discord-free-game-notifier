# Discord Free Game Notifier

Discord Free Game notifier is a utility you can which will notify you if there is free games and/or demos available.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used to scrape the the the games from the freebie articles from [gg.deals](https://www.https://gg.deals//).

This takes advantage of discord webhooks, all you need is a channel webhook url to properly set the utility up, you can learn more about discord webhooks by clicking [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

Since the deals.gg "Today" articles are filtered by the current day in UTC, this script should be schedule to run as a cron job right before. 30 minutes beforehand should be good enough to get all the articles of the day. You can learn more about setting up cron jobs below.

### Installing and running

* Clone this respository
    * HTTPS: `https://github.com/AlexTuTruong/discord-free-game-notifier.git`
    * SSH: `git@github.com:AlexTuTruong/discord-free-game-notifier.git`
    * Github CLI: `gh repo clone AlexTuTruong/discord-free-game-notifier`
* Navigate to the src folder in this repository
    * `cd /path/to/folder/src`
* Install the dependencies
    * `pip install -r requirements.txt`
* Configure your `.env` file
    * You can create a `.env` file or rename the `.env.example` file which already exists within the util folder
        * `WEBHOOK_URL="https://discord.com/api/webhooks/discord_webhook/url_goes_here"`
* Run the application
    * You would probably want to run this as a cron job on a server at a set time everyday to notify you appropriately
        *  But to run the script itself, lets say to test it, you can enter `python3 main.py`
    * To schedule a cron job to run the script:
        * Make the script executable: `chmod +x main.py`
        * Open the crontab file: `crontab -e`
        * Add a cron job entry: `30 19 * * * /path/to/main.py` 
            * Note that this example sets the script to run everyday at 7:30PM EST, you can read [this](https://phoenixnap.com/kb/set-up-cron-job-linux) for further cronjob configuration information
        * Save and exit the crontab file
        * Verify the cron job: `crontab -l` and check if your cron job is there

You can run a cron job on a service like [modal](https://modal.com/) if you don't have a server or computer you'd like to run this on

## Output

Script being run:

```
/free-game-bot/src$ python3 main.py
[2024-08-29 01:24:15] gg.deals response: 200
[2024-08-29 01:24:15] Pinging users | Status: 204
[2024-08-29 01:24:15] FREE Disney Epic Mickey: Rebrushed demo is now available! | Status: 204
[2024-08-29 01:24:16] FREE Tropico 4 on GOG for a limited time | Status: 204
```

Recieved message:

![Discord alert screenshot](https://github.com/user-attachments/assets/a51fb877-c554-4596-a3b5-8103146fce10)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
