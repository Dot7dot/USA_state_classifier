import json
import re


with open('FollowersUSA_All_Zone.json', 'r', encoding = 'utf-8') as f:
    followers = json.load(f)

num=0
datalist=[]

for f in followers:
    '''k = bool(re.search('USA|United States of America|America|'
                    #    以下各州
                       'Alabama|Ala\.|AL|Montgomery|Alaska|AK|Alaska|Arizona|AZ|Ariz\.|Arkansas|AR|Ark\.|'
                       'California|CA|Calif\.|Colorado|CO|Colo\.|'
                       'Connecticut|CT|Conn\.|Delaware|DE|Del\.|Florida|FL|Fla\.|Georgia|GA|Ga\.|Hawaii|HI|Hawaii|'
                       'Idaho|ID|Idaho|Illinois|IL|Ill\.|Indiana|IN|Ind\.|Iowa|IA|Iowa|Kansas|KS|Kans\.|'
                       'Kentucky|KY|Ky\.|Louisiana|LA|La\.|Maine|ME|Maine|Maryland|MD|Md\.|Massachusetts|MA|Mass\.|'
                       'Michigan|MI|Mich\.|Minnesota|MN|Minn\.|Mississippi|MS|Miss\.|Missouri|MO|Mo\.|'
                       'Montana|MT|Mont\.|Nebraska|NE|Neb\.|Nebr\.|Nevada|NV|Nev\.|New Hampshire|NH|N\.H\.|'
                       'New Jersey|NJ|N\.J\.|New Mexico|NM|N\.Mex\.|New York|NY|N\.Y\.|North Carolina|NC|N\.C\.|'
                       'North Dakota|ND|N\.Dak\.|Ohio|OH|Ohio|Oklahoma|OK|Okla\.|Oregon|OR|Ore\.|Oreg\.|'
                       'Pennsylvania|PA|Pa\.|Rhode Island|RI|R\.I\.|South Carolina|SC|S\.C\.|South Dakota|SD|S\.Dak\.|'
                       'Tennessee|TN|Tenn\.|Texas|TX|Tex\.|Texas|Utah|UT|Utah|Vermont|VT|Vt\.|Virginia|VA|Va\.|'
                       'Washington|WA|Wash\.|West|Virginia|WV|W\.Va\.|Wisconsin|WI|Wis\.|Wisc\.|Wyoming|WY|Wyo\.|'
                    #    以下各州首府
                       'Montgomery|Juneau|Little Rock|Sacramento|Denver|Hartford|Dover|Tallahassee|Atlanta|Honolulu|'
                       'Boise|Springfield|Indianapolis|Des Moines|Topeka|Frankfort|Baton Rouge|Augusta|Annapolis|Boston|'
                       'Lansing|St\. Paul|Jackson|Jefferson City|Helena|Lincoln|Carson City|Concord|Trenton|Santa Fe|'
                       'Albany|Raleigh|Bismarck|Columbus|Oklahoma City|Salem|Harrisburg|Providence|Columbia|Pierre|'
                       'Nashville|Austin|Salt Lake City|Montpelier|Richmond|Olympia|Charleston|Madison|Cheyenne|'''
    alabama = bool(re.search('(A|a)labama|Ala\.|, AL|Montgomery', f['location']))
    alaska = bool(re.search('(A|a)laska|Juneau|, AK', f['location']))
    arizona = bool(re.search('(A|a)rizona|, AZ|Ariz\.|Phoenix', f['location']))
    arkansas = bool(re.search('(A|a)rkansas|, AR|Ark\.|Little Rock', f['location']))
    california = bool(re.search('(C|c)alifornia|, CA|Calif\.|Sacramento.', f['location']))
    colorado = bool(re.search('(C|c)olorado|, CO|Colo\.|Denver', f['location']))
    connecticut = bool(re.search('(C|c)onnecticut|, CT|Conn\|Hartford', f['location']))
    delaware = bool(re.search('(D|d)elaware|, DE|Del\.|Dover', f['location']))
    florida = bool(re.search('(F|f)lorida|, FL|Fla\.|Tallahassee', f['location']))
    georgia = bool(re.search('(G|g)eorgia|, GA|, Ga\.|Atlanta', f['location']))
    hawaii = bool(re.search('(H|h)awaii|, HI|Honolulu', f['location']))
    idaho = bool(re.search('(I|i)daho|, ID|Idaho|Boise', f['location']))
    illinois = bool(re.search('(I|i)llinois|, IL|Ill\.|Springfield', f['location']))
    indiana = bool(re.search('(I|i)ndiana|, IN|Ind\.|Indianapolis', f['location']))
    iowa = bool(re.search('(I|i)owa|, IA|Des Moines', f['location']))
    kansas = bool(re.search('(K|k)ansas|, KS|Kans\.|Topeka', f['location']))
    kentucky = bool(re.search('(K|k)entucky|, KY|Ky\.|Frankfort', f['location']))
    louisiana = bool(re.search('(L|l)ouisiana|, LA|La\.|Baton Rouge', f['location']))
    maine = bool(re.search('(M|m)aine|, ME|Augusta', f['location']))
    maryland = bool(re.search('(M|m)aryland|, MD|Md\.|Annapolis', f['location']))
    massachusetts = bool(re.search('(M|m)assachusetts|, MA|Mass\.|Boston', f['location']))
    michigan = bool(re.search('(M|m)ichigan|, MI|Mich\.|Lansing', f['location']))
    minnesota = bool(re.search('(M|m)innesota|, MN|Minn\.|Saint Paul', f['location']))
    mississippi = bool(re.search('(M|m)ississippi|, MS|Miss\.|Jackson', f['location']))
    missouri = bool(re.search('(M|m)issouri|, MO|Mo\.|Jefferson City', f['location']))
    montana = bool(re.search('(M|m)ontana|, MT|Mont\.|Helena', f['location']))
    nebraska = bool(re.search('(N|n)ebraska|, NE|Neb\.|Nebr\.|Lincoln', f['location']))
    nevada = bool(re.search('(N|n)evada|, NV|Nev\.|Carson City', f['location']))
    newhampshire = bool(re.search('new hampshire|New Hampshire|, NH|N\.H\.|Concord', f['location']))
    newjersey = bool(re.search('new jersey|New Jersey|, NJ|N\.J\.|Trenton', f['location']))
    newmexico = bool(re.search('new mexico|New Mexico|, NM|N\.Mex\.|Santa Fe', f['location']))
    newyork = bool(re.search('new york|New York|, NY|N\.Y\.|Albany', f['location']))
    northcarolina = bool(re.search('north carolina|North Carolina|, NC|N\.C\.|Raleigh', f['location']))
    northdakota = bool(re.search('north dakota|North Dakota|, ND|N\.Dak\.|Bismarck', f['location']))
    oklahoma = bool(re.search('(O|o)klahoma|, OK|Okla\.|Oklahoma City', f['location']))
    ohio = bool(re.search('(O|o)hio|, OH|Columbus', f['location']))
    oregon = bool(re.search('(O|o)regon|, OR|Ore\.|Oreg\.|Salem', f['location']))
    pennsylvania = bool(re.search('(P|p)ennsylvania|, PA|Pa\.|Harrisburg', f['location']))
    rhodeisland = bool(re.search('rhode island|Rhode Island|, RI|R\.I\.|Providence', f['location']))
    southcarolina = bool(re.search('south carolina|South Carolina|, SC|S\.C\.|Columbia', f['location']))
    southdakota = bool(re.search('south dakota|South Dakota|, SD|S\.Dak\.|Pierre', f['location']))
    tennessee = bool(re.search('(T|t)ennessee|, TN|Tenn\.|Nashville', f['location']))
    texas = bool(re.search('(T|t)exas|, TX|Tex\.|Austin', f['location']))
    utah = bool(re.search('(U|u)tah|, UT|Salt Lake City', f['location']))
    vermont = bool(re.search('(V|v)ermont|, VT|Vt\.|Montpelier', f['location']))
    virginia = bool(re.search('(V|v)irginia|, VA|Va\.|Richmond', f['location']))
    washington = bool(re.search('(W|w)ashington|, WA|Wash\.|Olympia', f['location']))
    westvirginia = bool(re.search('west virginia|West Virginia|, WV|W\.Va\.|Charleston', f['location']))
    wisconsin = bool(re.search('(W|w)isconsin|, WI|Wis\.|Wisc\.|Madison', f['location']))
    wyoming = bool(re.search('(W|w)yoming|, WY|Wyo\.|Cheyenne', f['location']))
    usa = bool(re.search('USA|United States of America|(A|a)merica|United States', f['location']))

    if(usa):
        num += 1
        data = dict(account = f['account'],id = f['id'], name = f['name'] , location = f['location'], count = num )
        datalist.append(data)

state='usa'
with open('Followers_of_' + state + '.json', 'w', encoding='utf-8') as f:
    json.dump(datalist, f, ensure_ascii=False, indent=4)


