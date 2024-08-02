# This Program is Provides Live and Latest feed of CRICBUZZ.com using its API 

from requests import get
from pprint import PrettyPrinter

headers = {
	"x-rapidapi-key": "8d3df960a7msh8389ffa2274ac32p12e98ajsn75a7052dd155",
	"x-rapidapi-host": "crickbuzz-official-apis.p.rapidapi.com"
}
printer = PrettyPrinter()

# It Provides all the Feed Over the Home Page of CricBuzz Site LatestNews and ScoreBoard
def HomeFeed():
    url = "https://crickbuzz-official-apis.p.rapidapi.com/home"
   
    data = get(url, headers=headers).json()
    print('''
    1) Latest News
    2) ScoreBoard
     ''')
    x=int(input("Choose the Index of the Above Mentioned :"))
    if (x==1):
        hm=data['homepage']
        #print(hm)
        for i,n in enumerate(hm):
            print(f"{i+1}:  News Report    : {n.get('stories',{}).get('analyticsTag',{})}")
            print(f"    Context        : {n.get('stories',{}).get('context',{})}")
            print(f"    Head Line      : {n.get('stories',{}).get('headline',{})}")
            print(f"    Intro          : {n.get('stories',{}).get('intro',{})}")
            print(f"    NewsId         : {n.get('stories',{}).get('itemId',{})}")
            print()
    elif(x==2):
        mtc=data['matches']
        for i,n in enumerate(mtc):
            print(f"{i+1}: MatchInfo :","\n")
            print(f"    Match Discription   :{n.get('match',{}).get('matchInfo',{}).get('matchDesc',{})}")
            print(f"    Match Format        :{n.get('match',{}).get('matchInfo',{}).get('matchFormat',{})}")
            print(f"    Match ID            :{n.get('match',{}).get('matchInfo',{}).get('matchId',{})}")
            print(f"    Match Type          :{n.get('match',{}).get('matchInfo',{}).get('matchType',{})}")
            print(f"    Series              :{n.get('match',{}).get('matchInfo',{}).get('seriesName',{})}")
            print(f"    Current Status      :{n.get('match',{}).get('matchInfo',{}).get('shortStatus',{})}")
            print(f"    State               :{n.get('match',{}).get('matchInfo',{}).get('state',{})}")
            print(f"    Final Status        :{n.get('match',{}).get('matchInfo',{}).get('status',{})}")

            print("\nTeams & Venue :\n") 
            print(f"    {n.get('match',{}).get('matchInfo',{}).get('team1',{}).get('teamName',{})} vs {n.get('match',{}).get('matchInfo',{}).get('team2',{}).get('teamName',{})}")
            print(f"        City    :{n.get('match',{}).get('matchInfo',{}).get('venueInfo',{}).get('city',{})}")
            print(f"        Stadium :{n.get('match',{}).get('matchInfo',{}).get('venueInfo',{}).get('ground',{})}")

            print("\nScorecard :\n")
            print(f"             {n.get('match',{}).get('matchInfo',{}).get('team1',{}).get('teamSName',{})} | {n.get('match',{}).get('matchInfo',{}).get('team2',{}).get('teamSName',{})}")
            print(f"            ------------")
            print(f"    Runs    : {n.get('match',{}).get('matchScore',{}).get('team1Score',{}).get('inngs1',{}).get('runs','--')} | {n.get('match',{}).get('matchScore',{}).get('team2Score',{}).get('inngs1',{}).get('runs','--')}")
            print(f"    Wickets : {n.get('match',{}).get('matchScore',{}).get('team1Score',{}).get('inngs1',{}).get('wickets','--')} | {n.get('match',{}).get('matchScore',{}).get('team2Score',{}).get('inngs1',{}).get('wickets','--')}")
            print(f"    Overs   : {n.get('match',{}).get('matchScore',{}).get('team1Score',{}).get('inngs1',{}).get('overs','--')} | {n.get('match',{}).get('matchScore',{}).get('team2Score',{}).get('inngs1',{}).get('overs','--')}")

            
            print()
    else:
        print("Pls Enter the Valid Response!")
        return HomeFeed()
# Here We are Capturing the Live Feed Of the Matches that are happening Currently and the Upcomming Matches 
def matchesfeed():
    print('''
    1) Live Matches
    2) Upcomming Matches
    ''')
    x=int(input("Choose the Index of the Above Mentioned : "))
    if (x==1):
        url = "https://crickbuzz-official-apis.p.rapidapi.com/matches/live"
        data = get(url, headers=headers).json()
        print("\nLive Matches\n")
        for i in data['typeMatches']:
            print(f"Match Type    :{i['matchType']}")
            ab=i['seriesMatches']
            for j in ab:
                print(f"Series Name   :{j.get('seriesAdWrapper',{}).get('seriesName')}")
                for m,n in enumerate(j.get('seriesAdWrapper').get('matches')):
                    print(f"{m+1}: MatchInfo\n")
                    print(f"    Match Discription   :{n.get('matchInfo',{}).get('matchDesc',{})}")
                    print(f"    Match Format        :{n.get('matchInfo',{}).get('matchFormat',{})}")
                    print(f"    Match ID            :{n.get('matchInfo',{}).get('matchId',{})}")
                    print(f"    Series              :{n.get('matchInfo',{}).get('seriesName',{})}")
                    print(f"    State               :{n.get('matchInfo',{}).get('state',{})}")
                    print(f"    Status              :{n.get('matchInfo',{}).get('status',{})}")


                    print("\n  Teams & Venue :\n") 
                    print(f"        {n.get('matchInfo',{}).get('team1',{}).get('teamName',{})} vs {n.get('matchInfo',{}).get('team2',{}).get('teamName',{})}")
                    print(f"        City    :{n.get('matchInfo',{}).get('venueInfo',{}).get('city',{})}")
                    print(f"        Stadium :{n.get('matchInfo',{}).get('venueInfo',{}).get('ground',{})}")

                    print("\n  Scorecard :\n")
                    print(f"             {n.get('matchInfo',{}).get('team1',{}).get('teamSName',{})} | {n.get('matchInfo',{}).get('team2',{}).get('teamSName',{})}")
                    print(f"            ------------")
                    print(f"    Runs    : {n.get('matchScore',{}).get('team1Score',{}).get('inngs1',{}).get('runs','--')} | {n.get('matchScore',{}).get('team2Score',{}).get('inngs1',{}).get('runs','--')}")
                    print(f"    Wickets : {n.get('matchScore',{}).get('team1Score',{}).get('inngs1',{}).get('wickets','--')} | {n.get('matchScore',{}).get('team2Score',{}).get('inngs1',{}).get('wickets','--')}")
                    print(f"    Overs   : {n.get('matchScore',{}).get('team1Score',{}).get('inngs1',{}).get('overs','--')} | {n.get('matchScore',{}).get('team2Score',{}).get('inngs1',{}).get('overs','--')}")
                    print()
    elif(x==2):
        url = "https://crickbuzz-official-apis.p.rapidapi.com/matches/upcoming/"
        print("\nUpcomming Matches\n")
        print('''
        1: International
        2: League
        3: Domestic
        4: Women
              ''')
        r=int(input("Choose the Index of the Above Mentioned : "))
        print()
        if r==1:
            feed='International'
        elif r==2:
            feed='League'
        elif r==3:
            feed='Domestic'
        elif r==4:
            feed='Women'
        else:
            print("Pls Enter the Valid Response!")
            return matchesfeed()
    
        data = get(url, headers=headers).json()
        for i in data['typeMatches']:
            if i['matchType']==feed:
                ab=i['seriesMatches']
                for j in ab:
                    print(f"Series Name   :{j.get('seriesAdWrapper',{}).get('seriesName')}")
                    for m,n in enumerate(j.get('seriesAdWrapper').get('matches')):
                    
                        print(f"{m+1}: MatchInfo\n")
                        print(f"    Match Discription   :{n.get('matchInfo',{}).get('matchDesc',{})}")
                        print(f"    Match Format        :{n.get('matchInfo',{}).get('matchFormat',{})}")
                        print(f"    Match ID            :{n.get('matchInfo',{}).get('matchId',{})}")
                        print(f"    Series              :{n.get('matchInfo',{}).get('seriesName',{})}")
                        print(f"    State               :{n.get('matchInfo',{}).get('state',{})}")
                        print(f"    Final Status        :{n.get('matchInfo',{}).get('status',{})}")


                        print("\n  Teams & Venue :\n") 
                        print(f"        {n.get('matchInfo',{}).get('team1',{}).get('teamName',{})} vs {n.get('matchInfo',{}).get('team2',{}).get('teamName',{})}")
                        print(f"        City    :{n.get('matchInfo',{}).get('venueInfo',{}).get('city',{})}")
                        print(f"        Stadium :{n.get('matchInfo',{}).get('venueInfo',{}).get('ground',{})}")
                        print()
    else:
        print("Pls Enter the Valid Response!")
        return matchesfeed()

# Here We are Displaying the Latest News Report and Summary 
def news():
    url = "https://crickbuzz-official-apis.p.rapidapi.com/news"

    data = get(url, headers=headers).json()
    c=data['storyList']
    for i,n in enumerate(c):
        print(f"{i+1}:",f"Context      :{n.get('story',{}).get('context',{})}")
        print(f"   News Summary :{n.get('story',{}).get('coverImage',{}).get('caption',{})}")
        print(f"   Head Line    :{n.get('story',{}).get('hline',{})}")
        print(f"   News ID      :{n.get('story',{}).get('coverImage',{}).get('id',{})}")
        print(f"   Source       :{n.get('story',{}).get('coverImage',{}).get('source',{})}")
        print()


# Here We are Taking Out the Latest Ranking Of the Players and Teams
def iccrank():
    print('''
    1: Batsman
    2: Bowler 
    3: All Rounder
    4: Teams
    ''')
    x=int(input("Choose the Index No. :"))
    if(x==1):
        url = "https://crickbuzz-official-apis.p.rapidapi.com/rankings/batsman/"
        
    elif(x==2):
        url = "https://crickbuzz-official-apis.p.rapidapi.com/rankings/bowlers/"
    elif(x==3):
        url = "https://crickbuzz-official-apis.p.rapidapi.com/rankings/allrounders/"
    elif(x==4):
        url = "https://crickbuzz-official-apis.p.rapidapi.com/rankings/team/"
    else:
        print("Pls Enter the Valid No.!")
        iccrank()
    
    fmt=input("Enter the Format type (test/odi/t20) :").lower()
    cat=input("Enter Category (men/women):").lower()
    querystring={"formatType":fmt,cat:"1"}
    data = get(url, headers=headers,params=querystring).json()
    print()
    if(x==4):
        rk=data.get('rank')
        for i in rk:
            print(f"Rank    :{i.get('rank')}")
            print(f"Name    :{i.get('name')}")
            print(f"Matches :{i.get('Matches')}")
            print(f"Points  :{i.get('points')}")
            print(f"Rating  :{i.get('rating')}")

            print()
    else:
        rk=data.get('rank')
        for i in rk:
            print(f"Rank    :{i.get('rank')}")
            print(f"Name    :{i.get('name')}")
            print(f"Country :{i.get('country')}")
            print(f"Average :{i.get('avg')}")
            print(f"Rating  :{i.get('rating')}")
            print(f"Trend   :{i.get('trend')}")

            print()



# Main
def main():
    print("                        WELCOME TO CRICBUZZ API                 ")
    while True:
        print("--------------------------------------------------------------")
        print('''
        1: Home
        2: Matches
        3: News
        4: ICC Rankings
        
''')
        x=input("Choose Index from Above and q(to Quit):")
        if(x.isdigit()):
            x=int(x)
            if(x==1):
                HomeFeed()
            elif(x==2):
                matchesfeed()
            elif(x==3):
                news()
            elif(x==4):
                iccrank()
            else:
                print("Pls Enter the Correct Index!!")
                continue
        elif(x=='q'):
            break
        else:
            print("Pls Enter the Correct Index!!!")
            continue

main()


