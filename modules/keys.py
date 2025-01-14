from libqtile.lazy import lazy
from libqtile.config import KeyChord, Key

home = "/home/jomor"
mod = "mod4"
terminal = "kitty"
flameshot = f"{home}/flameshot.sh"
emacs = "emacsclient -c -a 'emacs'"
#emacse = "emacsclient --eval '(emacs-everywhere)'"
emacsclient = f"{home}/.nix-profile/bin/emacs --daemon"
#agenda = "emacsclient -c '/home/moore/org/20230619122239-agenda.org'"
#grabcolor = "grabc | xclip -sel clip"

keys = [

    #Rofi
    Key(["mod1"], "space", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mod], "p", lazy.spawn("rofi-pass"), desc="spawn rofi-pass"),
    Key([mod], "c", lazy.spawn("rofi -show calc"), desc="spawn rofi-calc"),

    KeyChord(["control"], "space", [
    Key([], "b", lazy.spawn(f"rofi -show file-browser-extended -file-browser-dir {home}/3D/Blender")),
    Key([], "h", lazy.spawn(f"rofi -show file-browser-extended -file-browser-dir {home}/3D/Houdini")),
    Key([], "p", lazy.spawn(f"rofi -show file-browser-extended -file-browser-dir {home}/Pictures")),
    ]),
    #Terminal
    Key([mod, "mod1"], "Return", lazy.spawn(terminal), desc="Launch terminal window"),
    #Emacs
    Key([mod], "e", lazy.spawn(emacs), desc="launch emacs"),
    #Key([mod,"mod1"], "e", lazy.spawn(emacse), desc="launch emacs everywhere"),
    Key(["control", "mod1"], "e", lazy.spawn(emacsclient), desc="launch emacsclient"),
    #File mangers
    Key([mod, "mod1"], "f", lazy.spawn('thunar'), desc="launch GUI file manager"),
    Key([mod, "shift"], "f", lazy.spawn([terminal, "-e", "ranger"]), desc="launch term file manager"),
    #Web Browsers
    Key([mod], "b", lazy.spawn('firefox'), desc="launch web browser"),
    Key([mod, "mod1"], "b", lazy.spawn('qutebrowser'), desc="launch alt web browser"),
    #Utility
    Key([mod], "s", lazy.spawn(flameshot), desc="draw screenshot"),

    Key([mod], "g", lazy.spawn('kcolorchooser'), desc="color chooser"),
    #Misc
    Key([mod], "d", lazy.spawn('discord'), desc="launch discord"),
    Key([mod], "m", lazy.spawn('spotify'), desc="launch spotify"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "l", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, "mod1"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioPlay",lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext",lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev",lazy.spawn("playerctl previous")),
]
