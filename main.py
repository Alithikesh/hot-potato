timer = 0

def on_forever():
    global timer
    timer = randint(5, 15)
    basic.show_icon(IconNames.CHESSBOARD)
    while timer > 0:
        timer += -1
        basic.pause(1000)
    basic.show_icon(IconNames.NO)
    music._play_default_background(music.built_in_playable_melody(Melodies.WAWAWAWAA),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.builtin_playable_sound_effect(soundExpression.sad),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
