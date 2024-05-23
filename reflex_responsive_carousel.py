from reflex import Var
import reflex as rx
from typing import Any, Dict, List, Optional, Set, Union, Literal, Callable
from types import SimpleNamespace
from reflex.utils import imports


"""Literal variables values"""
literal_axis_var=Literal["horizontal","vertical"]
literal_vertical_swipe_var=Literal["natural","standard"]

"""Responsive Carousel Class"""
class ResponsiveCarousel(rx.Component):
    library = "react-responsive-carousel"
    tag = "Carousel"

    """responsive carousel components"""
    axis:Var[literal_axis_var]
    auto_play:Var[bool]
    center_mode:Var[bool]
    center_slide_percentage:Var[float]
    infinite_loop:Var[bool]
    labels:Var[rx.Component]
    on_click_item:Var[Optional[Callable]]
    on_swipe_start:Var[Optional[Callable]]
    on_swipe_end:Var[Optional[Callable]]
    on_swipe_move:Var[Optional[Callable]]
    show_arrows:Var[bool]
    swipeable:Var[bool]
    use_keyboard_arrows:Var[bool]
    width:Var[Union[str,float]]
    height:Var[Union[str,float]]
    vertical_swipe:Var[literal_vertical_swipe_var]

    """import react carousel styles"""
    def add_imports(self):
        return {"":["react-responsive-carousel/lib/styles/carousel.min.css"]}
    
responsive_carousel=ResponsiveCarousel.create

