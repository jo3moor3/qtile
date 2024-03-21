from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.command import lazy
from .keys import keys, mod
group_names = ["1","2","3","4","5"]
groups = []

for i in range (len(group_names)):
    groups.append(Group(name = group_names[i]))

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

        Key([mod, "mod1"], "l", lazy.screen.next_group(), desc="Switch to next group"),
        Key([mod, "mod1"], "h", lazy.screen.prev_group(), desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

groups.append(ScratchPad("scratchpad",[

    DropDown("termup", "kitty", opacity = 0.85,),

    DropDown("term", "kitty",
        height = 0.9, width = 0.6, x = 0.2, y = 0, opacity = 0.95, warp_pointer = True,),

    DropDown("email", "/usr/bin/thunderbird",
        height = 0.8, width = 0.8, x = 0.1, y = 0.1, opacity = 0.95, warp_pointer = True,),

    DropDown("files", "kitty -e ranger",
        height = 0.8, width = 0.8, x = 0.1, y = 0.1, opacity = 0.95, warp_pointer = True,),

    DropDown("audio", "pavucontrol",
        height = 0.45, width = 0.4, x = 0.3, y = 0.1, opacity = 0.95, warp_pointer = True,)
        ]))

keys.extend([
        Key([mod], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([mod, "shift"], "Return", lazy.group['scratchpad'].dropdown_toggle('termup')),
        Key([mod], "f", lazy.group['scratchpad'].dropdown_toggle('files')),
        Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle('email')),
        Key([mod], "a", lazy.group['scratchpad'].dropdown_toggle('audio')),
        ])
