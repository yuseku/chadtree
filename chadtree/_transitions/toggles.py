from pynvim import Nvim
from pynvim_pp.lib import s_write

from ..registry import rpc
from ..settings.localization import LANG
from ..settings.types import Settings
from ..state.next import forward
from ..state.types import State
from ..version_ctl.git import status
from ..version_ctl.types import VCStatus
from .types import Stage


@rpc(blocking=False, name="CHADtoggle_hidden")
def c_hidden(nvim: Nvim, state: State, settings: Settings, is_visual: bool) -> Stage:
    """
    Toggle hidden
    """

    new_state = forward(state, settings=settings, show_hidden=not state.show_hidden)
    return Stage(new_state)


@rpc(blocking=False, name="CHADtoggle_follow")
def c_toggle_follow(
    nvim: Nvim, state: State, settings: Settings, is_visual: bool
) -> Stage:
    """
    Toggle follow
    """

    new_state = forward(state, settings=settings, follow=not state.follow)
    s_write(nvim, LANG("follow_mode_indi", follow=str(new_state.follow)))
    return Stage(new_state)


@rpc(blocking=False, name="CHADtoggle_version_control")
def c_toggle_vc(nvim: Nvim, state: State, settings: Settings, is_visual: bool) -> Stage:
    """
    Toggle version control
    """

    enable_vc = not state.enable_vc
    vc = status() if enable_vc else VCStatus()
    new_state = forward(state, settings=settings, enable_vc=enable_vc, vc=vc)
    s_write(nvim, LANG("version_control_indi", enable_vc=str(new_state.enable_vc)))
    return Stage(new_state)
