from hecate.bridge.base import Bridge


class MoireBridge:

    key_actions = {
        "up": Bridge.move_up,
        "down": Bridge.move_down,
        "left": Bridge.move_left,
        "right": Bridge.move_right,
        "=": Bridge.zoom_in,
        "-": Bridge.zoom_out,
        "[": Bridge.speed_down,
        "]": Bridge.speed_up,
        "spacebar": Bridge.toggle_pause,
        "f12": Bridge.toggle_sysinfo,
        "escape": Bridge.exit_app,
    }