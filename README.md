# Building your own Twitter quote bot

* Create an account for your bot
* Go to the [Delevopers Portal](https://developer.twitter.com/en/portal), scroll to the bottom and get started with a Free account (It allows to make up to 1500 posts per month, which translates to approximately a post every 30 minutes)
* It'll ask you to write a text with 250 characters about the intended use of the API, just describe the bot until it hits the minimum
* Your dashboard will already show a Project and App created for you with a random name, you can rename both of these if you want but it's also not necessary

## Gathering quotes

This can be done in any way you want. My personal strategy is to set up a Google Forms to receive submissions from anyone who wishes to make a contribution. Just be cautious of how you store and format the quotes, since they'll have to fit into a JSON file. More on the formatting below.


## Build a quote bot from this template

* Click on **Use this template** and **Create new repository**

* Download the your newly created repository into your computer so you can edit the files

This can be done by clicking **Code > Download ZIP** or if you're familiar with the command line just `git clone your-repo-url`. More on cloning remote repositories [here](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories).


* Using a text editor ([VSCode](https://code.visualstudio.com/), [Sublime](https://www.sublimetext.com/) or even the built-in text editor, just please do not use MS Word), edit "quotes.json" to include the quotes you want. Change the keys ("pots" and "losa") to the categories you want. It should look like this:

```
{
  "key1": [
      "quote1",
      "quote2"
	],
	"key2": [
      "quote1",
      "quote2"
	]
}
```

You can add as many keys as you want. If you want them to be randomly picked from a single pile, put all quotes inside a single key, which can be called "quotes" for easy access. In that case, you'll need to also change the `post_quote()` function in `func.py` to:

```
def post_quote():
	quotes = data["quotes"]
	random_index = random.randint(0, len(quotes)-1)
	quote = book_quotes[random_index]
	r = bot.create_tweet(text=quote)
	return None
```

**Be careful if your quotes include quotation marks**. Since the delimiter for the quotes is also "" this can lead to breaks in the code. All quotation marks that you wish to be part of the quote must be added as `\"` so the code knows to read it as part of the string. You can use [an online JSON formatter](https://jsonformatter.curiousconcept.com/) to make sure everything is okay.

* Once your desired changes to `quotes.json` and `func.py` have been made, reupload the files to the repository with the same name (I am aware that this is not the best practice for a Git repository. You can do this the correct way, by commiting the changes on your local repo and pushing it into Github or even making a new branch and creating a pull request (overkill imo, but this tutorial is meant to help people with no programming skills, so mind your business). If you wish to learn how to submit these changes through the command line on your computer, check this [tutorial](https://docs.github.com/en/get-started/using-git).

## Set up the enviroment secrets

* On your GitHub repository, go to **Settings > Secrets and variables > Actions**

* Click on **Manage environment secrets**

* Create new environment called **login** (If there's already an environment with that name created, click on it and ignore this step)

* From your [Developer Portal dashboard](https://developer.twitter.com/en/portal/dashboard), click on your App and go to **Keys and Tokens**

* Regenerate the **Consumer Keys** and keep the window open while you add those to GitHub

* Inside your environment, click **Add secret** and add your **API Key** as `CONSUMER_KEY` and **API Key Secret** as `CONSUMER_SECRET`

* Back in the Devoloper Portal, regenerate the **Access Token and Secret** 
Make sure they say **Created with Read and Write permissions**. If that's not the case, go to the App's **Settings** page and scroll to the bottom, where there should be an option for setting up you **User authentication settings**.

* Add the **Access Token** as secret on Github with the name `ACCESS_TOKEN` and the **Access Secret** as `ACCESS_TOKEN_SECRET`

Once you create the secrets it's not possible to access them anymore. If you wish to edit them, you'll have to generate new tokens and keys from the Developer dashboard. 

## Scheduling and deployment

* Edit the schedule on `post.yml` inside the folder `.github/workflows` to the cron schedule you want. This change can be made directly in the Github editor, by clicking on the file and on the pencil on the top right corner. Cron schedules follow the syntax `minute hour day(month) month day(week)` and you can test your schedule with [this helper](https://crontab.guru/). As an example:

```
on:
  schedule:
    - cron: '30 * * * *' # posts every hour at minute 30
```
```
on:
  schedule:
    - cron: '0 * * * *' # posts every hour at minute 0
```
```
on:
  schedule:
    - cron: '*/30 * * * *' # posts every 30 minutes
```
```
on:
  schedule:
    - cron: '0 */2 * * *' # posts every two hours
```
```
on:
  schedule:
    - cron: '0 6,18 * * *' # posts at 6 AM and 6 PM
```

A lot of GitHub Actions are schedule to run on the hour, which might cause delays on the bot. If you wish to curb that, set a different minute for the post, such as `- cron: '47 * * * *' # posts every hour at minute 47`.

## Known problems and troubleshoot

* The Twitter API doesn't allow for duplicate tweets and might skip a scheduled post occasionaly. The code somewhat accounts for that, but not in a elegant or 100% foolproof way. A better solution is in the works.


Check the tab **Actions** to see if your bot ran the workflow correctly. Any doubts or issues can be posted [here](https://github.com/juniscoding/rowanbot_twt/issues).
