# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Slithera", image = "images/slithera.jpg", color = "#26c952")
define d = Character("Bouldoug", color = "#bf6f2e")
define f = Character("Firetta", color = "#fc1e4b")
define resultText = Character(kind=nvl)
default SandD = 0 #counts positive choices for Slithera and Bouldoug. 2 is required to display their good ending.
default FandD = 0 #counts positive choices for Firetta and Bouldoug. 2 is required to display their good ending.
default SandF = 0 #counts positive choices for Slithera and Firetta. 2 is required to display their good ending.



# The game starts here.

label start:

    play music "gameMusic.ogg"

    #character introductions
    scene space_bg:
        xysize(1280,720)
    with fade

    "Welcome to your brand new job as a Galactic Mediator!"
    "It is your mission to spread peace and settle disputes among your assigned planets. This is accomplished by meeting with each planet's 
    assigned representative and hearing out their issues, then offering your guidance."
    "Try your best to encourage peaceful conflict resolution, and help foster cooperation!"
    "Now, let's meet your assigned planets."

    show planet_placeholder:
        yalign 0.5
        xalign 0.5

    with dissolve

    pause 1.0

    "This is Reptalia, a humid and wet planet. It is home to the Scalians, a bidepal snake-like species who value order and logic. They tend to
    keep things neat and well kept, and hold themselves in high regard."

    show slithera at center:
        zoom 0.6
    with dissolve

    s "Greetings Mediator. I am Slithera, representative of the prosperous planet Reptalia. I hope you will work as hard as I for the future 
    of all Scalians."
    s "Our two sister planets can be... obtuse... when attempting negotiation. I trust your diplomatic skills will show them the benefits of 
    allying with Reptalia."
    s "...Or at least teach them better manners."

    hide slithera with dissolve
    pause .5

    hide planet_placeholder with dissolve
    pause 1.0

    show planet_placeholder2:
        yalign 0.5
        xalign 0.5

    with dissolve

    pause 1.0

    "Next is the planet Dustux, aptly named due to its harsh desert-like surface. It is home to the Boulderans, a species of sentient boulder
    people made of rocks and stones." 
    "Boulderans tend to be loud, messy, and like to keep to themselves. They can be stubborn when it comes
    to change."

    show bouldoug at center:
        zoom 0.6      
        yalign 1.0
    with dissolve

    d "Hmm... Me Bouldoug not see you before. You must be peace person Bouldoug was told to meet."
    d "Bouldoug think peace boring... prefer smashing rocks!"
    d "... "
    d "But it Bouldoug's job to be here, so Bouldoug promise not to smash stuff during meeting."

    hide bouldoug with dissolve
    pause .5

    hide planet_placeholder2 with dissolve

    pause 1.0

    show planet_placeholder3:
        yalign 0.5
        xalign 0.5

    with dissolve

    pause 1.0

    "Finally is the planet Magmus, a fiery world of lava, stone, and metal. It is home to the Flamites, a species of sentient flames who inhabit metal 
    braziers as a form of clothing."
    "Flamites are an easy going people that don't often take things too seriously. They won't go out of their way to meet new species, but 
    are always open to new friendships."

    show firetta at center:
        zoom 0.55   
        yalign 1.0
    with dissolve

    f "What's up? I'm Firetta."
    f "My other buds in the Magmus government said I should keep things formal, soooo... "
    "Firetta pulls out a small sheet of metal with some notes burned onto it."
    f "*Ahem* Greetings, Galactic Mediator! I am Firetta, representative of the great people of Magmus - the Flamites! Together, I hope... "
    "Firetta trails off as she seems to get bored, then tosses her notes aside."
    f "Blah blah blah, you get it. I'll see you around, peacemaster."
    
    #fade to black for next scene
    scene black:
        xysize(1280,720)

    #first meeting
    image logo text = Text("First Meeting", size=60)
    show logo text:
        yalign(0.5)
        xalign(0.5)
    
    with Fade(2.0, 2.0, 2.0)
 
    pause 2

    #scene bg room
    scene space_bg:
        xysize(1280,720)
    

    show planet_placeholder:
        yalign 0.5
        xalign 0.5

    with fade

    pause 1.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show slithera at left:
        zoom 0.6
        #xalign 0.03
    with dissolve
        

    #First problem for meeting 1

    s "Greetings Mediator. My negotiations with the Boulderans have met an unfortunate standstill, as such I am seeking your council."
    s "I wish to establish a new trade route with Dustux, as the planet's unique metals would be perfect for constucting more durable housing 
    for Scalians. The storms on Reptalia can get quite intense, if you weren't aware."
    s "However, the Boulderans are hesitant to part with their metals - despite not using them for much as far as I can tell. I am unsure 
    as to how to proceed with our negotiations."

    menu:
        extend ""
        "Suggest that Slithera should insist the metals would be of great use to the Scalians":            
            jump neg_1

        "Suggest that Slithera should ask the Boulderans if there is anything they need":
            jump pos_1


    label pos_1:
        $ menu_flag = True
        $ SandD += 1 #one positive choice made, need two for good ending
            
        s "The Boulderans are stubborn and will likely insist they need nothing from us. However, if you believe this is the best course of 
        action then I shall heed your advice. I shall begin bombarding Bouldoug with questions at once."
        resultText "Once Slithera's mind is set to something, she will not stop until her goal is met. She pestered Bouldoug with questions to 
        find a suitable trade offer until he finally thought of something." 
        resultText "It turns out that scale lotion - a Scalian specialty used to soften 
        hard scales - does wonders for a Boulderan's rough skin. A deal was struck, and Slithera's new trade route came to fruition."
        jump meet1_prob2

    label neg_1:
        #show slithera mad
        $ menu_flag = True
        
        s "Indeed, I don't think the Boulderans quite grasp how useful their metals would be to us. I shall redouble my efforts at once."
        s "The Boulderans don't seem too terribly bright... perhaps I should bring pictures?"
        resultText "Despite Slithera's renewed efforts, the Boulderans remained firm in their stance on the trade route - they were 
        uninterested in parting with their metals."
        resultText "On the bright side, the Boulderans did seem to enjoy Slithera's colorful illustrations."
        jump meet1_prob2

    #problem 2 meeting 1
    label meet1_prob2:
        scene space_bg:
            xysize(1280,720)
        

        show planet_placeholder2:
            yalign 0.5
            xalign 0.5

        with Fade(1.0, 1.0, 1.0)

        pause 1.0

        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.

        show bouldoug at right:
            zoom 0.6      
            yalign 1.0
            
        with dissolve
            

        #Second problem for meeting 1

        d "Bouldoug have no problem for peace person to fix, but Bouldoug do have exciting weekend plans!"
        d "Boulderans hear Magmus have mighty forges to smelt any metal. We go and demand fire people let us use forges! It is Boulderans' 
        rocky right to forge sacred metal!"

        menu:
            extend ""
            "Suggest Bouldoug should request a meeting with Firetta to discuss this first":
                jump pos_2

            "Say that the Flamites should honor Boulderan rights":            
                jump neg_2

        label pos_2:
            $ menu_flag = True
            $ FandD += 1 #one positive choice made, need two for good ending
                
            d "Talk to fire lady first? Hrm, Bouldoug no good at phone calls, but will call fire lady if peace person say so."
            d "Bouldoug will explain good to fire lady! Bouldoug have way with words, after all."
            nvl clear
            resultText "Despite hating being on video calls, Bouldoug gave Firetta a call to discuss the Boulderan's desire to use the 
            forges of Magmus."
            resultText "Excited by the prospect of seeing new and alien metals smelted and forged on their very own planet, the Flamites were 
            delighted to help the Boulderans." 
            resultText"There was only one condition: the Flamites would work alonside the Boulderans the whole time."
            resultText "Despite their rough and tough exterior, the Boulderans were as giddy as the Flamites that weekend."
            jump meet2_prob1

        label neg_2:
            #show slithera mad
            $ menu_flag = True
            
            d "Peace person understand Boulderan rights well! Forges of Magmus will be good use in hands of Boulderans!"
            nvl clear
            resultText "Like bulls in a china shop, the Boulderans arrived on Magmus that weekend making quite a racket."
            resultText "They marched proudly up to the legendary forges, demanding to be allowed entry to smelt their sacred ores. But they 
            were turned away, being told only those granted special permission were allowed in."
            resultText "Furious, the Boulderans made quite the scene before begrudgingly returning to their ship and flying home." 
            resultText"In contrast with their usual jovial nature, the Flamites were noticably more tense for the rest of that weekend."
            jump meet2_prob1


    #meeting 2
    label meet2_prob1:
        #fade to black for next scene
        scene black:
            xysize(1280,720)

        #first meeting
        image logo text2 = Text("Second Meeting", size=60)
        show logo text2:
            yalign(0.5)
            xalign(0.5)
        
        with Fade(2.0, 2.0, 2.0)
    
        pause 2

        #scene bg room
        scene space_bg:
            xysize(1280,720)
        

        show planet_placeholder3:
            yalign 0.5
            xalign 0.5

        with fade

        pause 1.0

       

        show firetta at right:
            zoom 0.55   
            yalign 1.0
        with dissolve
            

        #First problem for meeting 2

        f "Hey, what's going on peacemaster? I haven't been up to much, but there is something I wanted your opinion on."
        f "So, you've met that Slithera chick right? Well, she's tryna set up some trade routes with Magmus. She loves her trade routes, huh?"
        f "Anyways, she was listing off rule after rule and I could barely get a word in. All these restrictions and regulations she wants to 
        throw in make me feel like she's tryna take over or something."
        f "The Flamite people usually just kinda go with the flow, y'know? We're pretty chill like that, but this stuff with the trade route 
        is rubbing me the wrong way. I'm just not sure how to approach this."

        menu:
            extend ""
            "Suggest Firetta meet Slithera halfway and compromise":
                jump pos_3

            "Encourage Firetta to stand firm on her opinions":            
                jump neg_3




        label pos_3:
            $ menu_flag = True
            $ SandF += 1 #one positive choice made, need two for good ending
                
            f "I suppose you're right, although I was kinda hoping you would totally agree with me. Haha!"
            f "Talking with Slithera can be like talking to a brick wall sometimes, but I do think this trade route could really help us both. 
            I'll do my best to meet her halfway. Later!"
            nvl clear
            resultText "Firetta approached her next meeting with Slithera with a more open mindset, seeking to follow the advice she had 
            been given." 
            resultText "By giving a little ground in their negotiation to Slithera, Firetta was able to reach an agreement that was amicable
            to both parties. The trade route was successfully agreed upon."
            resultText "Feeling accomplished, Firetta suggested her and Slithera go get some lava tea - a Flamite classic. Slithera agreed 
            \"out of curtesy,\" but was secretly very excited."
            jump meet2_prob2

        label neg_3:
            #show slithera mad
            $ menu_flag = True
            
            f "You know what, you're right! If the Scalians really want this trade route set up, then they're gonna have to do it my way. Thanks boss!"
            nvl clear
            resultText "With renewed fiery determination, Firetta met once again with Slithera to discuss the possible trade route. Despite her 
            newfound vigor, Firetta's firm stance did not produce the desired results."
            resultText "Firetta's unmoving stance on the matter seemed to only encourage Slithera's insistance on her rules and regulations. 
            In the end, no agreement could be reached."
            jump meet2_prob2

        #problem 2 meeting 2
        label meet2_prob2:
            scene space_bg:
                xysize(1280,720)
            

            show planet_placeholder2:
                yalign 0.5
                xalign 0.5

            with Fade(1.0, 1.0, 1.0)

            pause 1.0

            # This shows a character sprite. A placeholder is used, but you can
            # replace it by adding a file named "eileen happy.png" to the images
            # directory.

            show bouldoug at right:
                zoom 0.6      
                yalign 1.0
                
            with dissolve
                

            #Second problem for meeting 2

            d "Me Bouldoug not happy! Snake lady and snake lady friends visit Bouldoug's planet for peace meeting thingy." 
            d "Snake people no stop complaining about planet being too dry, and no understand greatness of ancient Boulderan pile of rocks! 
            Grr, it make Bouldoug upset!"

            menu:
                extend ""
                "Tell Bouldoug that he can't force his perspective on the Scalians":            
                    jump neg_4

                "Remind Bouldoug that they have a different culture and biology, and that he should try to relate to them":
                    jump pos_4


            label pos_4:
                $ menu_flag = True
                $ SandD += 1 #one positive choice made, need two for good ending
                    
                d "Hmm... Snake people very different from Bouldoug's people. Snake planet very wet too. Maybe more water for Snakies?"
                d "Hrm... Bouldoug do best to keep Snakies wet next time. And Bouldoug get greatest scholar to teach Snakies culture... 
                Bouldoug's uncle Boulderek!"
                d "Large thank you, peace person!"
                nvl clear
                resultText "The next week, when Slithera and the visiting Scalians returned once again, Bouldoug made sure to prepare a warm welcome."
                resultText "Bouldoug assigned a few Boulderans to accompany their visitors, carrying large coolers with a variety of drinks." 
                resultText "He also supplied the scalians with umbrellas and large hats, and even installed a pool in their apartment."
                resultText "Bouldoug's uncle Boulderek, a renowned Boulderan scholar, gave the Scalians a few informative lectures on Boulderan
                culture. Slithera, a scholar herself, was particularly invested."
                jump meet3_prob1

            label neg_4:
                #show slithera mad
                $ menu_flag = True
                
                d "Peace person right. If snake people no understand Boulderans, Bouldoug not care. Bouldoug have better things to do!"
                nvl clear
                resultText "Bouldoug's next meeting with the visiting Scalians went mostly the same. Bouldoug made no effort to understand 
                or compensate the Scalians, and instead only greeted them with snappy impatience."
                resultText "As a result, the Scalians left Dustux with the uncomfortable feeling they weren't wanted."
                jump meet3_prob1
    
    
        label meet3_prob1:
            #fade to black for next scene
            scene black:
                xysize(1280,720)

            #first meeting
            image logo text3 = Text("Third Meeting", size=60)
            show logo text3:
                yalign(0.5)
                xalign(0.5)
            
            with Fade(2.0, 2.0, 2.0)
        
            pause 2

            #scene bg room
            scene space_bg:
                xysize(1280,720)
            

            show planet_placeholder:
                yalign 0.5
                xalign 0.5

            with fade

            pause 1.0

        

            show slithera at left:
                zoom 0.6
                #xalign 0.03
            with dissolve
                

            #First problem for meeting 3

            s "Greetings Mediator. I have come to seek your wise council once again."
            s "I have noticed a severe disparity in the levels of education on Magmus. Only a small portion of Flamites receive a satisfactory 
            education, while the majority are lucky to have any at all."
            s "On Reptalia, education and study are the backbones of our people. I believe better education could benefit Magmus greatly, and 
            in turn make the Flamites a greater ally to the Scalians. I am unsure if I should act on this."


            menu:
                extend ""
                "Suggest the Scalians could build new schools and train new Flamite teachers":
                    jump pos_5

                "Tell Slithera that the Flamites should be allowed to grow their society on their own":            
                    jump neg_5




            label pos_5:
                $ menu_flag = True
                $ SandF += 1 #one positive choice made, need two for good ending
                    
                s "An excellent idea Mediator, I was thinking similarly. With a more even distribution of schools and qualified instructors, 
                Magmus will surely flourish and grow."
                s "It is only logical that an ally of the Scalians should be granted the same basic rights to a satisfactory education. I 
                shall reach out to the Flamites on the matter immediately."
                nvl clear
                resultText "With Slithera's insistence on an improved educational system, the Flamites could see little reason to say no." 
                resultText "With the aid of the Scalians, construction on new schools and the training of new Flamite teachers began. 
                Soon, nearly every town on Magmus had a shiny new school."
                resultText "The Flamites quickly grew more advanced as a species, finding new passions in their recently learned sciences. 
                The majority of Magmus found themselves enjoying a higher quality of life."
                resultText "An initiative to give young Flamites field trips to Reptalia was also started, spearheaded by Slithera."
                jump meet3_prob2

            label neg_5:
                #show slithera mad
                $ menu_flag = True
                
                s "Perhaps you are correct, Mediator. My duty is to my people, and I may have been over-reaching with my aspirations."
                s "I shall turn my attention back to more pressing matters on Reptalia. Good day, Mediator."
                nvl clear
                resultText "In the end, no action was taken by the Scalians to improve the access and quality of education on Magmus. Only 
                a small portion of Flamites were still lucky enough to gain an education."
                resultText "The relationship between Reptalia and Magmus never grew much more intimate than simple trade routes."
                jump meet3_prob2

            #problem 2 meeting 3
            label meet3_prob2:
                scene space_bg:
                    xysize(1280,720)
                

                show planet_placeholder3:
                    yalign 0.5
                    xalign 0.5

                with Fade(1.0, 1.0, 1.0)

                pause 1.0

                # This shows a character sprite. A placeholder is used, but you can
                # replace it by adding a file named "eileen happy.png" to the images
                # directory.

                show firetta at right:
                    zoom 0.55   
                    yalign 1.0
                with dissolve
                    

                #Second problem for meeting 3

                f "Hey peacemaster, got a situation for ya."
                f "Sooo, I don't know how much you know about Flamite biology, but we mainly eat coal."
                f "..."
                f "Hey, don't knock it 'till you try it!"
                f "Anyway, here's the issue. An unexpected volcano eruption wiped out one of our major mining and storage sites for coal. 
                A lot of my people are going hungry right now. I just... don't know what to do."
                f "We don't have enough coal to feed everyone right now, and people are going to suffer. I didn't know what to do, so I figured
                I would get your opinion..."

                menu:
                    extend ""
                    "Tell Firetta her people are strong and will find a way":            
                        jump neg_6

                    "Encourage Firetta to reach out to the Boulderans for help":
                        jump pos_6


                label pos_6:
                    $ menu_flag = True
                    $ FandD += 1 #one positive choice made, need two for good ending
                        
                    f "The rocky guys? You really think they could help?"
                    f "Well, I guess they are MADE of rocks, so maybe they have some extra coal laying around we can trade for. At least I 
                    can probably get some advice on quickly getting a new mine set up..."
                    f "*Sigh* Alright, I'll give Dougy a call and see what I can do. Thanks peacemaster, I feel a little better about all this."
                    nvl clear
                    resultText "Firetta contacted Bouldoug looking for help, and although Bouldoug didn't like being called \"Dougy,\" Firetta
                    was suprised to find the Boulderans eager to help. After all, rocks ARE their specialty."
                    resultText "Relief aid in the form of generous amounts of coal were delivered to the starving Flamites, and mass hunger
                    was avoided."
                    resultText "While they were on Magmus, the Boulderans gave the Flamites some insight into Boulderan mining methods. They
                    even helped set up new mineshafts before returning home."
                    resultText "As Firetta discovered, it turns out Boulderans eat coal as well. Thankful for his help, Firetta promised to take
                    Bouldoug out for a nice pile of coal once things settled down."
                    jump ending

                label neg_6:
                    #show slithera mad
                    $ menu_flag = True
                    
                    f "*Sigh* I was afraid you would say that..."
                    f "The math just doesn't work out. We can't feed everyone with what we have left."
                    f "The Flamites are a strong people, I know we can make it through this. I just... hope we can get new mines ready soon."
                    f "...I'll be seeing you then."
                    nvl clear
                    resultText "Without any extra resources or support, the Flamites suffered a mass starvation. Many did not survive."
                    resultText "Despite Firetta's efforts, food was not evenly distributed. It was determined that an equal amount of food for
                    everyone was simply not enough, and the many in the lower class went hungry."
                    jump ending

            label ending:
                stop music fadeout 3.0
                
                nvl clear
                #fade to black for next scene
                scene black:
                    xysize(1280,720)

                #first meeting
                image logo text4 = Text("Epilogue", size=60)
                show logo text4:
                    yalign(0.5)
                    xalign(0.5)
                
                with Fade(2.0, 2.0, 2.0)
            
                pause 2

                play music "ending.ogg"
                scene black 
                if SandD == 2:
                    scene slithera_and_bouldoug:
                        xysize(1280,720)
                    with Fade(1.0,1.0,2.0)
                    "Although very different species, the Scalians and Boulderans managed to find common ground with one another. Through 
                    efforts to better understand one another, the people of Reptalia and Dustux formed a rock solid relationship."
                    "Bouldoug likes to get Slithera a new hat whenever she visits, and Slithera always brings the latest brand of scale lotion."
                
                if FandD == 2:
                    scene bouldoug_and_firetta:
                        xysize(1280,720)
                    with Fade(1.0,1.0,2.0)
                    "The Boulderans and Flamites, two relatively reclusive species, had come to form a strong bond with one another. By asking
                    for help and responding with compassion, the two previously distant species found they had much in common."
                    "Firetta never forgot her promise, and took Bouldoug out for Magmus's finest coal dishes."

                if SandF == 2:
                    scene slithera_and_firetta:
                        xysize(1280,720)
                    with Fade(1.0,1.0,2.0)
                    "Despite their peoples having very different attitudes and views, the Scalians and Flamites came to respect and work well
                    with one another. Through the Scalians involvement in Magmus, the Flamites grew through better education and new resources."
                    "In return, the Scalians found the Flamites to be rubbing off on them and learned to live a bit livelier."
                    "Slithera and Firetta like to enjoy tea together on the weekends."

                

            
                if (SandD + FandD + SandF) == 6:
                    
                    scene space_bg:
                        xysize(1280,720)
                    with Fade(1.0,1.0,2.0)

                    show planet_placeholder3 at right:
                        xalign(0.7)
                        yalign(0.5)
                    with dissolve
                    pause 1.0
                    show planet_placeholder2 at center:
                        xalign(0.5)
                        yalign(0.5)
                    with dissolve
                    pause 1.0
                    show planet_placeholder at left:
                        xalign(0.3)
                        yalign(0.5)
                    with dissolve
                    pause 1.0
                    "Reptalia, Dustux, and Magmus have entered a new age of interplanetary cooperation. Through compassion, sympathy, and 
                    kindness, the once distant peoples have found themselves closer than ever."
                    "And none of this progress could have been made without you. By encouraging peaceful and thoughtful actions you have 
                    brought these people together, and improved the lives of many."
                    "Good work!"

                elif (SandD + FandD + SandF) == 0:
                    scene space_bg:
                        xysize(1280,720)
                    with Fade(1.0,1.0,2.0)
                    resultText "Despite your best efforts, your council did not provide the desired results to your assigned planets."
                    resultText "Tensions have risen between all three planets, and generally things are pretty bad."
                    resultText "...In other words, you're fired."

                #fade to black for next scene
                scene black:
                    xysize(1280,720)

                #first meeting
                image logo text5 = Text("The End", size=60)
                show logo text5:
                    yalign(0.5)
                    xalign(0.5)
                
                with Fade(2.0, 2.0, 2.0)
            
                pause 2
                scene black with fade
                stop music fadeout 2.0
                pause 2
                

    # This ends the game.

    return
