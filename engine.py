from __future__ import annotations

from typing import TYPE_CHECKING
import lzma
import pickle

import tcod.console
from tcod.map import compute_fov

from message_log import MessageLog
import exceptions
import render_functions

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap, GameWorld


class Engine:
    game_map: GameMap
    game_world: GameWorld

    def load_game(self, filename: str) -> None:
        """Load a previously saved game."""
        with open(filename, "rb") as f:
            load_data = pickle.loads(lzma.decompress(f.read()))

        # We loaded a new game. Start the engine with the new game data.
        self.game_world = load_data.game_world
        self.current_menu = load_data.current_menu
        self.message_log = load_data.message_log
        self.mouse_location = load_data.mouse_location
        self.player = load_data.player
        self.event_handler = load_data.event_handler
        self.game_map = load_data.game_map

        # We need to re-initialize the FOV, since the size of the map may have changed.
        self.update_fov()



    def __init__(self, player: Actor):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console) -> None:
        self.game_map.render(console)

        self.message_log.render(console=console, x=21, y=45, width=40, height=5)

        render_functions.render_bar(
            console=console,
            current_value=self.player.fighter.hp,
            maximum_value=self.player.fighter.max_hp,
            total_width=20,
        )

        render_functions.render_dungeon_level(
            console=console,
            dungeon_level=self.game_world.current_floor,
            location=(0, 47),
        )

        render_functions.render_names_at_mouse_location(console=console, x=21, y=44, engine=self)

    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)
