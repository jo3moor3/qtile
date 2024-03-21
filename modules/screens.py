from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

bcolor = "#2f343f"
backcolor = "#00000050"
#"#00000050"
screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background= bcolor),
                widget.Image(filename='~/.config/qtile/nix.png', margin=3, background= bcolor, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background= bcolor),
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background= bcolor),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground= bcolor
                       ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background= bcolor),
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground= bcolor
                       ),
                volume,
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground= bcolor,
                       ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground= bcolor
                       ),
                widget.Clock(format='%Y-%m-%d %a',
                             background= bcolor,
                             foreground='#9bd689'),
                widget.Clock(format='󰥔 %I:%M %p',
                             background= bcolor,
                             foreground='#ffffff'),
                                                widget.TextBox(

                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.dotfiles/bin/powermenu.sh'))
                    },
                    foreground='#e39378'
                )

            ],
            30,  # height in px
            background= backcolor  # background color
        ), ),
]
