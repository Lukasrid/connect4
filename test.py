import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('connect4_score')


def get_player_names():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    
    player1 = input("Enter name of player 1: ")
    player2 = input("Enter name of player 2: ")
    player1_and_2 = player1 + ',' + ' vs ' + ',' + player2

    players_combined = player1_and_2.split(",")

        

    return players_combined




def update_score_sheet(players):
    """
    Update sales worksheet, add new row with the list data provided
    """
    
    print("\nUpdating names...\n")
    sales_worksheet = SHEET.worksheet("score")
    sales_worksheet.append_row(players)
    print("Names updated.\n")


players = get_player_names()

update_score_sheet(players)