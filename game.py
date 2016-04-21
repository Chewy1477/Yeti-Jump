import pygame
import gamebox
import random

multiplier = 1
camera = gamebox.Camera(800,600)
character = gamebox.from_image(100,200,'http://www.illustrationsof.com/royalty-free-rf-yeti-clipart-illustration-by-cory-thoman-stock-sample-102505.jpg')
character.yspeed = 0
character.scale_by(.05)
b1 = gamebox.from_image(400,300, 'http://thumbs.dreamstime.com/z/christmas-snowflake-background-white-wallpaper-35056457.jpg')



walls = [
    gamebox.from_color(50,250, "black", 200, 10),
    gamebox.from_color(400,150, "black", 200, 10),
    gamebox.from_color(600,25, "black", 200, 10),
]

coins = [
    gamebox.from_color(75,400, "yellow", 10, 10),
    gamebox.from_color(160,200, "yellow", 10, 10),
    gamebox.from_color(280,250, "yellow", 10, 10)
]

enemy = [
]
counter = 0
lives = 3
character_score= 0
game_over = False
fail_over = False
start_game = False
def tick(keys):
    global start_game
    global game_over
    global fail_over
    b3= gamebox.from_text(400,300,"Welcome to Yeti Jump! Get 10 points to win!", "Arial", 40, 'red', italic=True)
    b4 = gamebox.from_text(400,400, "Press s to start!","Arial", 40, 'red', italic=True)
    camera.draw(b3)
    camera.draw(b4)
    if pygame.K_s in keys:
        start_game = True
    if start_game is True:
        if fail_over is False:
            if game_over is False:
                global counter
                global lives
                global character_score
                if pygame.K_RIGHT in keys:
                    character.x += 10
                if pygame.K_LEFT in keys:
                    character.x -= 10
                character.yspeed += 1
                character.y = character.y + character.yspeed
                camera.clear("cyan")
                camera.draw(b1)
                camera.draw("Lives: " + str(lives), "Arial", 24, "red", 100, 100)

                camera.draw(character)
                if character.y > 600 or 800 >= character.x <= 0:
                    lives -= 1
                    charater_score = 0
                    character.x = walls[-1].x
                    character.y = walls[-1].y
                    camera.draw(character)

                camera.draw("Character Score: "+ str(character_score), "Arial", 24, "red", 100, 30)

                camera.y -= 3
                b1.y = camera.y

                global counter
                counter += 1
                if counter % 50 == 0:
                    new_wall = gamebox.from_color(random.randint(100,700), camera.y-300,  "black", random.randint(100,250), 10)
                    walls.append(new_wall)
                    if character.y >= new_wall.y + 600 or character.x < 0 or character.x > 800     :
                        lives -= 1
                        character.x = walls[-1].x
                        character.y = walls[-1].y
                        camera.draw(character)
                if counter%40 == 0:
                    coins.append(gamebox.from_color(random.randint(100,550),(character.y-200),"yellow",10,10))
                for coin in coins:
                    camera.draw(coin)
                    if character.touches(coin):
                        coins.remove(coin)
                        coin_sound = gamebox.load_sound('http://theodoregray.com/PeriodicTable/Sounds/029.2.wav')
                        musicplayer0=coin_sound.play()
                        character_score += 1
                        camera.draw("Character Score: " + str(character_score), "Arial", 24, "red", 100, 30)

                if counter%45 == 0:
                    enemy.append(gamebox.from_color(random.randint(100,550),(character.y-200),"red",5,5))
                multiplier = 1
                for thing in enemy:
                    thing.x += 10*multiplier
                    if thing.x >500 or thing.x<300:
                        multiplier = multiplier*-1

                    camera.draw(thing)
                    if character.touches(thing):
                        enemy.remove(thing)
                        character_score -= 5
                        lives -= 1
                        camera.draw("Character Score: " + str(character_score), "Arial", 24, "red", 100, 30)

                for wall in walls:
                    if character.bottom_touches(wall):
                        character.yspeed = 0
                        if pygame.K_SPACE in keys:
                            character.yspeed = -20
                    if character.touches(wall):
                        character.move_to_stop_overlapping(wall)
                    camera.draw(wall)


                if lives == 0:
                    fail_over = True
                if character_score is 10:
                    game_over = True



            else:
                camera.clear("white")
                camera.draw("You Win! Snooooow good", "Arial", 30,"red", 400, 300)
                camera.draw("Press q to quit", "Arial", 30, "red", 400, 500)
                if pygame.K_q in keys:
                    gamebox.stop_loop()
        else:
            camera.clear('white')
            camera.draw("Sorry you lost!", "Arial", 30, "red", 400, 250)
            camera.draw("Press q to quit", "Arial", 30, "red", 400, 450)
   
            if pygame.K_q in keys:
                gamebox.stop_loop()
    camera.display()
ticks_per_second = 30


gamebox.timer_loop(ticks_per_second, tick)
