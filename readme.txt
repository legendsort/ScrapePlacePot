## COMMAND
    scrapy crawl placepot -a st=<start date> -a ed=<end date> -a course=<course name> -O <output file name>

    i.e. 
        scrapy crawl placepot -a st='15 April 2022' -a ed='21 April 2022' -a course=Cork -O output.csv

        output.csv
        
        race,time,course,distance,runners,favourite,placed,card_no,name
        Race 1,1:50,Cork,3m 80y,18,5,1st,14,Tenzing
        Race 1,1:50,Cork,3m 80y,18,5,2nd,21,Roped In
        Race 1,1:50,Cork,3m 80y,18,5,3rd,8,Friends N Commerce
        Race 2,2:25,Cork,2m,16,9,1st,12,Garcon Doux
        Race 2,2:25,Cork,2m,16,9,2nd,23,Contrapposto
        Race 2,2:25,Cork,2m,16,9,3rd,9,The Niffler (F)
        Race 2,2:25,Cork,2m,16,9,4th,21,Crescent Lake
        Race 3,2:59,Cork,2m 160y,6,6,1st,3,Kildorrery
        Race 3,2:59,Cork,2m 160y,6,6,2nd,4,R'evelyn Pleasure
        Race 4,3:34,Cork,3m,6,3,1st,4,Ifeoinly
        Race 4,3:34,Cork,3m,6,3,2nd,2,Carrig Wells
        Race 5,4:09,Cork,3m,8,3,1st,9,Its On The Line
        Race 5,4:09,Cork,3m,8,3,2nd,3,Earl Of Desmond (F)
        Race 5,4:09,Cork,3m,8,3,3rd,10,Plain Or Battered
        Race 6,4:44,Cork,2m 4f,5,4,1st,2,Down The Highway
        Race 6,4:44,Cork,2m 4f,5,4,2nd,4,Lord Schnitzel (F)
        Race 1,1:10,Cork,2m,16,8,1st,8,Prairie Dancer (F)
        Race 1,1:10,Cork,2m,16,8,2nd,9,Prince Of Verona
        Race 1,1:10,Cork,2m,16,8,3rd,14,Wee Willie Nail
        Race 2,1:45,Cork,2m 3f,17,6,1st,3,Copper Nation
        Race 2,1:45,Cork,2m 3f,17,6,2nd,5,Emily Roebling
        Race 2,1:45,Cork,2m 3f,17,6,3rd,16,Vibrance
        Race 3,2:20,Cork,2m,7,3,1st,5,Irascible
        Race 3,2:20,Cork,2m,7,3,2nd,1,Cash Back
        Race 4,2:55,Cork,2m 4f,14,1,1st,5,Grand Paradis
        Race 4,2:55,Cork,2m 4f,14,1,2nd,1,Aione (F)
        Race 4,2:55,Cork,2m 4f,14,1,3rd,6,Henry Star
        Race 5,3:30,Cork,3m,5,1,1st,1,Melon (F)
        Race 5,3:30,Cork,3m,5,1,2nd,4,Doctor Duffy
        Race 6,4:05,Cork,2m 3f,14,12,1st,9,Bois De Clamart
        Race 6,4:05,Cork,2m 3f,14,12,2nd,7,Happy Jacky
        Race 6,4:05,Cork,2m 3f,14,12,3rd,10,Bread And Butter
        Race 1,1:40,Cork,7f,15,16,1st,16,Toy (F)
        Race 1,1:40,Cork,7f,15,16,2nd,12,Esculenta
        Race 1,1:40,Cork,7f,15,16,3rd,3,Culcor
        Race 2,2:15,Cork,7f,16,4,1st,4,Run The Jewels (F)
        Race 2,2:15,Cork,7f,16,4,2nd,8,London Palladium
        Race 2,2:15,Cork,7f,16,4,3rd,12,Tooso
        Race 2,2:15,Cork,7f,16,4,4th,3,Florence Thompson
        Race 3,2:50,Cork,7f,17,16,1st,15,Punk Poet
        Race 3,2:50,Cork,7f,17,16,2nd,6,Yermanthere
        Race 3,2:50,Cork,7f,17,16,3rd,16,That's Just Dandy (F)
        Race 3,2:50,Cork,7f,17,16,4th,18,Breaking Story
        Race 4,3:25,Cork,1m 4f 25y,12,1,1st,1,Thunder Kiss (F)
        Race 4,3:25,Cork,1m 4f 25y,12,1,2nd,3,Annerville
        Race 4,3:25,Cork,1m 4f 25y,12,1,3rd,7,Pineapple Express
        Race 5,4:00,Cork,1m 2f 30y,15,19,1st,5,Ghasham
        Race 5,4:00,Cork,1m 2f 30y,15,19,2nd,13,Ruler Legend
        Race 5,4:00,Cork,1m 2f 30y,15,19,3rd,3,Bringbackmemories
        Race 6,4:35,Cork,1m 2f 30y,5,1,1st,1,French Claim (F)
        Race 6,4:35,Cork,1m 2f 30y,5,1,2nd,3,Sussex

