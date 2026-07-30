languages={}


TEXT={

"fa":{

"start":
"🤖 DANI BOT STUDIO",

"create":
"ساخت ربات",

"bots":
"ربات های من",

"language":
"تغییر زبان"

},


"en":{

"start":
"🤖 DANI BOT STUDIO",

"create":
"Create Bot",

"bots":
"My Bots",

"language":
"Language"

}

}



def get_language(user):

    return languages.get(
        user,
        "fa"
    )



def change_language(user):

    old=get_language(user)

    if old=="fa":
        languages[user]="en"

    else:
        languages[user]="fa"



def text(user,key):

    return TEXT[
        get_language(user)
    ][key]
