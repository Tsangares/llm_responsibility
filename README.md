# Quickstart

## Setup Dependencies

Install the dependencies using pip or conda. This project is using python3.13

    pip install -r requirements.txt

## Setup ApiKey

Setup a `.env` file with your OpenAI ApiKey as the environment variable: `OPENAI_API_KEY`.

## Running the code

Run `replications.ipynb` from top to bottom to see the results of the datasets in `dist`

Run `game_play.ipynb` to generate new results to `dist`.

# Notes on Running

At the beginning of the notebook in `game_play.ipynb`, there are parameters to change. If the game has less than 10 sessions, it will not save unless you change the flag `SAVE=TRUE`. All parameters are being manually saved into `yaml` for reference. Any new datasets generated are timestamped using a unix time for simplicity in chornologically ordering the datasets. Use the `yaml` reference file to infer what prompts you used and how many rounds or sessions were appropriately used. 


Please contact me if you have any questions; or make an issue. 
