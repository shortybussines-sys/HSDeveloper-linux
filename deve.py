import os
import sys
import json
import subprocess
import platform
import shutil
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


APP_NAME = "HSDeveloper"
APP_VERSION = "3.0"


def resource_path(filename: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)


LANG_DATA = {
    "Čeština": {
        "dashboard": "Dashboard",
        "builder": "Builder",
        "templates": "Šablony",
        "addons": "Doplňky",
        "guide": "Guide",
        "export": "Export",
        "settings": "Nastavení",
        "language": "Jazyk",
        "theme": "Motiv",
        "minecraft_version": "Minecraft verze",
        "script_type": "Typ skriptu",
        "project_name": "Název projektu",
        "prefix": "Prefix",
        "generate": "Vygenerovat",
        "copy": "Kopírovat",
        "save_sk": "Uložit .sk",
        "save_project": "Uložit projekt",
        "load_project": "Načíst projekt",
        "reset": "Reset",
        "live_preview": "Živý náhled",
        "welcome": "Vítej v HSDeveloperu",
        "welcome_desc": "Moderní studio pro tvorbu Minecraft Skript souborů, šablon a začátečnických helperů.",
        "template_hint": "Vyber typ skriptu, uprav nastavení a vpravo uvidíš výsledek.",
        "theme_dark": "Dark",
        "theme_light": "Light",
        "command_name": "Název commandu",
        "permission": "Permission",
        "cooldown": "Cooldown (sekundy)",
        "command_aliases": "Aliasy (oddělené čárkou)",
        "command_description": "Popis commandu",
        "message_self": "Zpráva sobě",
        "message_target": "Zpráva targetu",
        "use_target": "Povolit target hráče",
        "use_console": "Povolit konzoli",
        "world_only": "Pouze ve hře",
        "join_message": "Join zpráva",
        "quit_message": "Quit zpráva",
        "heal_mode": "Typ akce",
        "heal_mode_heal": "Heal",
        "heal_mode_feed": "Feed",
        "warp_name": "Název warpu",
        "warp_permission": "Permission warpu",
        "teleport_message": "Teleport zpráva",
        "reward_item": "Reward item",
        "reward_amount": "Počet itemů",
        "reward_message": "Reward zpráva",
        "kit_name": "Název kitu",
        "kit_items": "Itemy kitu (oddělené čárkou)",
        "kit_permission": "Permission kitu",
        "broadcast_message": "Broadcast zpráva",
        "announcement_name": "Název announce commandu",
        "home_name": "Název home",
        "gui_title": "Název GUI",
        "ticket_name": "Název ticket commandu",
        "report_name": "Název report commandu",
        "money_amount": "Částka",
        "template_search": "Hledat šablonu",
        "template_count": "Počet šablon",
        "status_ready": "Připraveno",
        "status_generated": "Skript vygenerován",
        "status_saved": "Projekt uložen",
        "status_loaded": "Projekt načten",
        "status_exported": "Skript uložen",
        "status_reset": "Reset hotov",
        "success": "Hotovo",
        "error": "Chyba",
        "file_saved": "Soubor byl uložen.",
        "project_saved": "Projekt byl uložen.",
        "project_loaded": "Projekt byl načten.",
        "copied": "Kód byl zkopírován do schránky.",
        "nothing_to_save": "Není co uložit.",
        "launcher": "Spustit Minecraft Launcher",
        "quick_actions": "Rychlé akce",
        "active_addons": "Aktivní doplňky",
        "guide_title": "Guide pro začátečníky",
        "guide_text": (
            "1. Začni jednoduchými commandy.\n"
            "2. Vždy mysli na permission a zprávy pro hráče.\n"
            "3. Nepřeháněj to s proměnnými, dokud jim nerozumíš.\n"
            "4. Testuj skripty po menších částech.\n"
            "5. Dávej pozor na kompatibilitu addonů.\n"
            "6. Používej přehledné názvy commandů a prefixů.\n"
            "7. U GUI a ticket systémů si naplánuj logiku předem.\n\n"
            "Co si pamatovat:\n"
            "- command /test:\n"
            "- on join:\n"
            "- on quit:\n"
            "- send \"zpráva\" to player\n"
            "- permission: plugin.node\n"
            "- if arg-1 is set:\n"
            "- teleport player to spawn\n\n"
            "Začátečnické rady:\n"
            "- Udělej si nejdřív malý cíl.\n"
            "- Používej malé skripty a testuj je.\n"
            "- Když se něco rozbije, hledej problém po blocích.\n"
            "- Nejdřív funkčnost, potom vzhled a extra funkce.\n"
            "- U templatek si vždy zkontroluj permission a texty."
        ),
        "settings_title": "Vzhled a chování",
        "select_theme": "Vyber vzhled aplikace",
        "select_lang": "Vyber jazyk aplikace",
        "preview_placeholder": "# Zde se zobrazí vygenerovaný Skript kód...",
        "script_command": "Command",
        "script_joinquit": "Join/Quit",
        "script_healfeed": "Heal/Feed",
        "script_warp": "Warp",
        "script_reward": "Reward",
        "script_kit": "Kit",
        "script_broadcast": "Broadcast",
        "script_home": "Home",
        "script_gui": "GUI",
        "script_ticket": "Ticket",
        "script_report": "Report",
        "script_money": "Money",
        "filter_all": "Vše",
    },
    "English": {
        "dashboard": "Dashboard",
        "builder": "Builder",
        "templates": "Templates",
        "addons": "Addons",
        "guide": "Guide",
        "export": "Export",
        "settings": "Settings",
        "language": "Language",
        "theme": "Theme",
        "minecraft_version": "Minecraft version",
        "script_type": "Script type",
        "project_name": "Project name",
        "prefix": "Prefix",
        "generate": "Generate",
        "copy": "Copy",
        "save_sk": "Save .sk",
        "save_project": "Save project",
        "load_project": "Load project",
        "reset": "Reset",
        "live_preview": "Live preview",
        "welcome": "Welcome to HSDeveloper",
        "welcome_desc": "Modern studio for creating Minecraft Skript files, templates, and beginner helpers.",
        "template_hint": "Choose a script type, customize it, and see the result on the right.",
        "theme_dark": "Dark",
        "theme_light": "Light",
        "command_name": "Command name",
        "permission": "Permission",
        "cooldown": "Cooldown (seconds)",
        "command_aliases": "Aliases (comma separated)",
        "command_description": "Command description",
        "message_self": "Self message",
        "message_target": "Target message",
        "use_target": "Allow player target",
        "use_console": "Allow console",
        "world_only": "Only in-game",
        "join_message": "Join message",
        "quit_message": "Quit message",
        "heal_mode": "Action type",
        "heal_mode_heal": "Heal",
        "heal_mode_feed": "Feed",
        "warp_name": "Warp name",
        "warp_permission": "Warp permission",
        "teleport_message": "Teleport message",
        "reward_item": "Reward item",
        "reward_amount": "Item amount",
        "reward_message": "Reward message",
        "kit_name": "Kit name",
        "kit_items": "Kit items (comma separated)",
        "kit_permission": "Kit permission",
        "broadcast_message": "Broadcast message",
        "announcement_name": "Announcement command name",
        "home_name": "Home name",
        "gui_title": "GUI title",
        "ticket_name": "Ticket command name",
        "report_name": "Report command name",
        "money_amount": "Amount",
        "template_search": "Search template",
        "template_count": "Template count",
        "status_ready": "Ready",
        "status_generated": "Script generated",
        "status_saved": "Project saved",
        "status_loaded": "Project loaded",
        "status_exported": "Script saved",
        "status_reset": "Reset complete",
        "success": "Done",
        "error": "Error",
        "file_saved": "File has been saved.",
        "project_saved": "Project has been saved.",
        "project_loaded": "Project has been loaded.",
        "copied": "Code copied to clipboard.",
        "nothing_to_save": "Nothing to save.",
        "launcher": "Open Minecraft Launcher",
        "quick_actions": "Quick actions",
        "active_addons": "Active addons",
        "guide_title": "Beginner Guide",
        "guide_text": (
            "1. Start with simple commands.\n"
            "2. Always think about permission nodes and messages.\n"
            "3. Do not overuse variables before you understand them.\n"
            "4. Test scripts in small parts.\n"
            "5. Watch addon compatibility.\n"
            "6. Use clear command and prefix names.\n"
            "7. Plan GUI and ticket logic before building.\n\n"
            "Remember:\n"
            "- command /test:\n"
            "- on join:\n"
            "- on quit:\n"
            "- send \"message\" to player\n"
            "- permission: plugin.node\n"
            "- if arg-1 is set:\n"
            "- teleport player to spawn\n\n"
            "Tips:\n"
            "- Decide what the script should do first.\n"
            "- Then choose the right template.\n"
            "- If something breaks, debug block by block.\n"
            "- Check permissions and messages every time."
        ),
        "settings_title": "Appearance and behavior",
        "select_theme": "Choose application theme",
        "select_lang": "Choose application language",
        "preview_placeholder": "# Generated Skript code will appear here...",
        "script_command": "Command",
        "script_joinquit": "Join/Quit",
        "script_healfeed": "Heal/Feed",
        "script_warp": "Warp",
        "script_reward": "Reward",
        "script_kit": "Kit",
        "script_broadcast": "Broadcast",
        "script_home": "Home",
        "script_gui": "GUI",
        "script_ticket": "Ticket",
        "script_report": "Report",
        "script_money": "Money",
        "filter_all": "All",
    }
}


class HSDeveloper(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME} {APP_VERSION}")
        self.geometry("1650x960")
        self.minsize(1320, 820)

        self.lang_name = "Čeština"
        self.lang = LANG_DATA[self.lang_name]
        self.current_theme = "Dark"
        self.current_page = "builder"
        self.preview_code = ""
        self.ui_icon = None
        self.window_icon_photo = None
        self.template_library = []
        self.template_search_var = tk.StringVar(value="")
        self.template_filter_var = tk.StringVar(value="all")
        self._theme_is_rebuilding = False
        self._template_search_trace_added = False

        self.mc_versions = [
            "1.16.5", "1.17", "1.18.2", "1.19.4",
            "1.20.1", "1.20.4", "1.20.6",
            "1.21", "1.21.1", "1.21.4", "1.21.8"
        ]

        self.script_type_values = [
            "script_command",
            "script_joinquit",
            "script_healfeed",
            "script_warp",
            "script_reward",
            "script_kit",
            "script_broadcast",
            "script_home",
            "script_gui",
            "script_ticket",
            "script_report",
            "script_money"
        ]

        self.addon_names = [
            "Skript", "SkBee", "SkQuery", "TuSKe", "skript-gui",
            "SkRayFall", "Skellett", "ItemsAdder", "PlaceholderAPI",
            "Vault", "MythicMobs", "ModelEngine", "Citizens", "WorldGuard"
        ]

        self.nav_buttons = {}
        self.addons = {}

        self.init_vars()
        self.setup_window_icon()
        self.load_ui_icon()
        self.build_template_library()
        self.apply_theme()
        self.build_ui()
        self.switch_page("builder")
        self.generate_script()
        self.set_status(self.L("status_ready"))
        self.bind_template_search_trace()

    def find_icon_path(self):
        for name in ("themes.png", "themes.ico"):
            path = resource_path(name)
            if os.path.exists(path):
                return path
        return None

    def setup_window_icon(self):
        self.window_icon_photo = None
        icon_path = self.find_icon_path()
        if not icon_path:
            return

        try:
            img = Image.open(icon_path)
            self.window_icon_photo = ImageTk.PhotoImage(img)
            self.iconphoto(True, self.window_icon_photo)
        except Exception:
            pass

        if platform.system() == "Windows" and icon_path.lower().endswith(".ico"):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

    def load_ui_icon(self):
        icon_path = self.find_icon_path()
        if not icon_path:
            self.ui_icon = None
            return

        try:
            image = Image.open(icon_path)
            self.ui_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(30, 30))
        except Exception:
            self.ui_icon = None

    def init_vars(self):
        self.project_name_var = tk.StringVar(value="MyHSProject")
        self.language_var = tk.StringVar(value=self.lang_name)
        self.theme_var = tk.StringVar(value="Dark")
        self.mc_version_var = tk.StringVar(value="1.21.8")
        self.script_type_var = tk.StringVar(value=self.L("script_command"))

        self.prefix_var = tk.StringVar(value="&8[&2HSDeveloper&8] &f")
        self.command_name_var = tk.StringVar(value="heal")
        self.permission_var = tk.StringVar(value="hsdeveloper.heal")
        self.cooldown_var = tk.StringVar(value="0")
        self.aliases_var = tk.StringVar(value="uzdravit,hp")
        self.command_description_var = tk.StringVar(value="Uzdraví hráče")
        self.message_self_var = tk.StringVar(value="&aHotovo.")
        self.message_target_var = tk.StringVar(value="&aByl jsi ovlivněn commandem.")
        self.use_target_var = tk.BooleanVar(value=True)
        self.use_console_var = tk.BooleanVar(value=False)
        self.world_only_var = tk.BooleanVar(value=True)

        self.join_message_var = tk.StringVar(value="&a%player% se připojil na server.")
        self.quit_message_var = tk.StringVar(value="&c%player% opustil server.")
        self.heal_mode_var = tk.StringVar(value="Heal")
        self.warp_name_var = tk.StringVar(value="spawn")
        self.warp_permission_var = tk.StringVar(value="hsdeveloper.warp.spawn")
        self.teleport_message_var = tk.StringVar(value="&aTeleportuji tě na warp.")
        self.reward_item_var = tk.StringVar(value="diamond")
        self.reward_amount_var = tk.StringVar(value="3")
        self.reward_message_var = tk.StringVar(value="&aZískal jsi odměnu.")
        self.kit_name_var = tk.StringVar(value="starter")
        self.kit_items_var = tk.StringVar(value="stone sword,bread,torch")
        self.kit_permission_var = tk.StringVar(value="hsdeveloper.kit.starter")
        self.broadcast_message_var = tk.StringVar(value="&6Server event právě začíná!")
        self.announcement_name_var = tk.StringVar(value="announce")
        self.home_name_var = tk.StringVar(value="home")
        self.gui_title_var = tk.StringVar(value="&8HS Menu")
        self.ticket_name_var = tk.StringVar(value="ticket")
        self.report_name_var = tk.StringVar(value="report")
        self.money_amount_var = tk.StringVar(value="100")

        for addon in self.addon_names:
            self.addons[addon] = tk.BooleanVar(value=(addon == "Skript"))

    def bind_template_search_trace(self):
        if not self._template_search_trace_added:
            self.template_search_var.trace_add("write", self.on_template_search_change)
            self._template_search_trace_added = True

    def on_template_search_change(self, *args):
        if self.current_page == "templates":
            self.switch_page("templates")

    def build_template_library(self):
        self.template_library = []

        def add_template(title, script_key, preset):
            self.template_library.append({
                "title": title,
                "script_key": script_key,
                "preset": preset,
                "category": script_key
            })

        command_templates = [
            ("Heal Command", "heal", "hs.heal"),
            ("Feed Command", "feed", "hs.feed"),
            ("Fly Command", "fly", "hs.fly"),
            ("God Command", "god", "hs.god"),
            ("Speed Command", "speed", "hs.speed"),
            ("Day Command", "day", "hs.day"),
            ("Night Command", "night", "hs.night"),
            ("Clear Chat", "clearchat", "hs.clearchat"),
            ("Ping Command", "ping", "hs.ping"),
            ("Workbench Command", "wb", "hs.workbench"),
            ("EnderChest Command", "ec", "hs.enderchest"),
            ("Hat Command", "hat", "hs.hat"),
            ("Trash Command", "trash", "hs.trash"),
            ("Suicide Command", "suicide", "hs.suicide"),
            ("Craft Command", "craft", "hs.craft"),
            ("Rename Command", "rename", "hs.rename"),
            ("Repair Command", "repair", "hs.repair"),
            ("Top Command", "top", "hs.top"),
            ("Back Command", "back", "hs.back"),
            ("Rules Command", "rules", "hs.rules"),
        ]
        for title, cmd, perm in command_templates:
            add_template(title, "script_command", {
                "command_name": cmd,
                "permission": perm
            })

        for name, cmd, perm, mode in [
            ("Heal Self", "heal", "hs.heal", "Heal"),
            ("Feed Self", "feed", "hs.feed", "Feed"),
            ("Staff Heal", "staffheal", "hs.staffheal", "Heal"),
            ("Staff Feed", "stafffeed", "hs.stafffeed", "Feed"),
            ("Quick Heal", "quickheal", "hs.quickheal", "Heal"),
            ("Quick Feed", "quickfeed", "hs.quickfeed", "Feed"),
            ("Arena Heal", "arenaheal", "hs.arenaheal", "Heal"),
            ("Event Feed", "eventfeed", "hs.eventfeed", "Feed"),
            ("VIP Heal", "vipheal", "hs.vipheal", "Heal"),
            ("VIP Feed", "vipfeed", "hs.vipfeed", "Feed"),
        ]:
            add_template(name, "script_healfeed", {
                "command_name": cmd,
                "permission": perm,
                "heal_mode": mode
            })

        for warp in [
            "spawn", "shop", "pvp", "mine", "arena", "event", "nether",
            "end", "parkour", "crate", "village", "forest", "desert",
            "ice", "lobby", "farm", "xp", "casino", "boats", "admin"
        ]:
            add_template(f"Warp {warp.title()}", "script_warp", {
                "warp_name": warp,
                "warp_permission": f"hs.warp.{warp}"
            })

        reward_items = [
            ("Diamond Reward", "diamond", "3"),
            ("Emerald Reward", "emerald", "5"),
            ("Gold Reward", "gold ingot", "10"),
            ("Iron Reward", "iron ingot", "16"),
            ("Food Reward", "bread", "12"),
            ("Torch Reward", "torch", "32"),
            ("Starter Reward", "stone sword", "1"),
            ("VIP Reward", "diamond", "12"),
            ("Daily Reward", "emerald", "2"),
            ("Vote Reward", "diamond", "1"),
        ]
        for title, item, amount in reward_items:
            add_template(title, "script_reward", {
                "command_name": title.lower().replace(" ", "_"),
                "permission": f"hs.reward.{title.lower().replace(' ', '')}",
                "reward_item": item,
                "reward_amount": amount
            })

        kits = [
            ("Starter Kit", "starter", "wooden sword,bread,torch"),
            ("Food Kit", "food", "bread,cooked beef,golden apple"),
            ("Tools Kit", "tools", "stone pickaxe,stone axe,stone shovel"),
            ("Miner Kit", "miner", "iron pickaxe,torch,bread"),
            ("PVP Kit", "pvp", "iron sword,golden apple,shield"),
            ("Archer Kit", "archer", "bow,arrow,leather helmet"),
            ("Builder Kit", "builder", "stone,oak planks,glass"),
            ("Farmer Kit", "farmer", "wheat seeds,carrot,potato,hoe"),
            ("VIP Kit", "vip", "diamond sword,diamond pickaxe,golden apple"),
            ("Legend Kit", "legend", "diamond sword,diamond chestplate,enchanted golden apple"),
        ]
        for title, kit, items in kits:
            add_template(title, "script_kit", {
                "kit_name": kit,
                "kit_permission": f"hs.kit.{kit}",
                "kit_items": items
            })

        broadcast_templates = [
            ("Event Announce", "announce", "&6Server event právě začíná!"),
            ("Restart Announce", "restart", "&cServer se brzy restartuje!"),
            ("Maintenance Announce", "maintenance", "&eServer je v údržbě."),
            ("Giveaway Announce", "giveaway", "&aPrávě začíná giveaway!"),
            ("Vote Announce", "vote", "&bNezapomeň hlasovat pro server!"),
            ("Discord Announce", "discord", "&9Připoj se na náš Discord!"),
            ("Rules Announce", "rulesannounce", "&ePřečti si pravidla serveru."),
            ("Update Announce", "updateannounce", "&aNa server přibyl nový update."),
            ("Shop Announce", "shopannounce", "&6Mrkni na server shop."),
            ("Stream Announce", "streamannounce", "&dMajitel právě streamuje."),
        ]
        for title, cmd, msg in broadcast_templates:
            add_template(title, "script_broadcast", {
                "announcement_name": cmd,
                "permission": f"hs.{cmd}",
                "broadcast_message": msg
            })

        for home in [
            "home", "base", "villagehome", "minehome", "farmhome",
            "castlehome", "skyhome", "deserthome", "icehome", "treehome"
        ]:
            add_template(f"{home.title()} Teleport", "script_home", {
                "home_name": home,
                "permission": f"hs.{home}"
            })

        gui_templates = [
            ("Main Menu GUI", "menu", "&8Main Menu"),
            ("Server GUI", "servermenu", "&8Server Menu"),
            ("Warp GUI", "warps", "&8Warp Menu"),
            ("Help GUI", "helpmenu", "&8Help Menu"),
            ("Admin GUI", "adminmenu", "&8Admin Panel"),
            ("Rewards GUI", "rewards", "&8Rewards"),
            ("Profile GUI", "profile", "&8Player Profile"),
            ("Vote GUI", "votemenu", "&8Vote Menu"),
            ("Shop GUI", "shopmenu", "&8Shop Menu"),
            ("Rules GUI", "rulesmenu", "&8Rules"),
        ]
        for title, cmd, gui_title in gui_templates:
            add_template(title, "script_gui", {
                "command_name": cmd,
                "permission": f"hs.{cmd}",
                "gui_title": gui_title
            })

        for ticket in [
            "ticket", "support", "helpop", "staffhelp", "bugticket",
            "appeal", "playerhelp", "contactstaff", "fastsupport", "urgenthelp"
        ]:
            add_template(f"{ticket.title()} System", "script_ticket", {
                "ticket_name": ticket,
                "permission": f"hs.{ticket}"
            })

        for report in [
            "report", "playerreport", "cheaterreport", "bugreport", "staffreport",
            "reportuser", "reporthack", "quickreport", "abusereport", "toxreport"
        ]:
            add_template(f"{report.title()} System", "script_report", {
                "report_name": report,
                "permission": f"hs.{report}"
            })

        money_templates = [
            ("Give Money 100", "givemoney100", "100"),
            ("Give Money 250", "givemoney250", "250"),
            ("Give Money 500", "givemoney500", "500"),
            ("Give Money 1000", "givemoney1000", "1000"),
            ("Daily Money", "dailymoney", "150"),
            ("Vote Money", "votemoney", "75"),
            ("Bonus Money", "bonusmoney", "300"),
            ("Event Money", "eventmoney", "500"),
            ("Starter Money", "startermoney", "200"),
            ("VIP Money", "vipmoney", "1000"),
        ]
        for title, cmd, amount in money_templates:
            add_template(title, "script_money", {
                "command_name": cmd,
                "permission": f"hs.{cmd}",
                "money_amount": amount
            })

        join_quit_templates = [
            ("Classic Join/Quit", "&a%player% se připojil.", "&c%player% odešel."),
            ("VIP Join/Quit", "&6VIP %player% se připojil.", "&6VIP %player% odešel."),
            ("Dark Join/Quit", "&8>> &a%player% joined", "&8<< &c%player% left"),
            ("Streamer Join/Quit", "&dStreamer %player% přišel!", "&dStreamer %player% odešel!"),
            ("Minimal Join/Quit", "&7+ %player%", "&7- %player%"),
            ("Modern Join/Quit", "&8[&a+&8] &f%player%", "&8[&c-&8] &f%player%"),
            ("Event Join/Quit", "&bEvent hráč %player% joined.", "&bEvent hráč %player% left."),
            ("Fantasy Join/Quit", "&5%player% vstoupil do světa.", "&5%player% opustil svět."),
            ("Red Join/Quit", "&c%player% joined RedZone.", "&c%player% left RedZone."),
            ("Blue Join/Quit", "&9%player% joined BlueZone.", "&9%player% left BlueZone."),
        ]
        for title, join_msg, quit_msg in join_quit_templates:
            add_template(title, "script_joinquit", {
                "join_message": join_msg,
                "quit_message": quit_msg
            })

    def apply_theme(self):
        ctk.set_appearance_mode("dark" if self.current_theme == "Dark" else "light")
        if self.current_theme == "Dark":
            self.colors = {
                "app": "#202123",
                "sidebar": "#171717",
                "topbar": "#202123",
                "card": "#2a2b32",
                "card_2": "#24252b",
                "entry": "#1c1d22",
                "preview": "#1e1f25",
                "border": "#3a3b43",
                "text": "#ececf1",
                "text_dim": "#a1a1aa",
                "accent": "#10a37f",
                "accent_hover": "#0e8f6f",
                "nav_hover": "#2d2f39",
                "nav_active": "#30323d"
            }
        else:
            self.colors = {
                "app": "#f7f7f8",
                "sidebar": "#ececf1",
                "topbar": "#ffffff",
                "card": "#ffffff",
                "card_2": "#f3f4f6",
                "entry": "#ffffff",
                "preview": "#f8fafc",
                "border": "#d7dbe2",
                "text": "#1f2937",
                "text_dim": "#6b7280",
                "accent": "#10a37f",
                "accent_hover": "#0e8f6f",
                "nav_hover": "#e8eaef",
                "nav_active": "#dde2ea"
            }
        self.configure(fg_color=self.colors["app"])

    def L(self, key):
        return self.lang.get(key, key)

    def build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, fg_color=self.colors["sidebar"], width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(20, weight=1)

        self.main = ctk.CTkFrame(self, fg_color=self.colors["app"], corner_radius=0)
        self.main.grid(row=0, column=1, sticky="nsew")
        self.main.grid_rowconfigure(1, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.build_sidebar()
        self.build_topbar()
        self.build_content()

    def build_sidebar(self):
        logo = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo.grid(row=0, column=0, sticky="ew", padx=18, pady=(18, 10))

        logo_top = ctk.CTkFrame(logo, fg_color="transparent")
        logo_top.pack(anchor="w")

        if self.ui_icon:
            self.logo_icon_label = ctk.CTkLabel(logo_top, text="", image=self.ui_icon)
            self.logo_icon_label.pack(side="left", padx=(0, 10))

        self.logo_title = ctk.CTkLabel(
            logo_top,
            text=APP_NAME,
            font=ctk.CTkFont(size=30, weight="bold"),
            text_color=self.colors["text"]
        )
        self.logo_title.pack(side="left")

        self.logo_sub = ctk.CTkLabel(
            logo,
            text="Minecraft Skript Studio",
            font=ctk.CTkFont(size=13),
            text_color=self.colors["text_dim"]
        )
        self.logo_sub.pack(anchor="w", pady=(6, 0))

        nav_keys = ["dashboard", "builder", "templates", "addons", "guide", "export", "settings"]
        for idx, key in enumerate(nav_keys, start=1):
            btn = ctk.CTkButton(
                self.sidebar,
                text=self.L(key),
                height=42,
                corner_radius=12,
                fg_color="transparent",
                hover_color=self.colors["nav_hover"],
                text_color=self.colors["text"],
                anchor="w",
                command=lambda k=key: self.switch_page(k)
            )
            btn.grid(row=idx, column=0, sticky="ew", padx=14, pady=5)
            self.nav_buttons[key] = btn

        self.launcher_btn = ctk.CTkButton(
            self.sidebar,
            text=self.L("launcher"),
            height=42,
            corner_radius=12,
            fg_color=self.colors["accent"],
            hover_color=self.colors["accent_hover"],
            text_color="white",
            command=self.launch_minecraft_launcher
        )
        self.launcher_btn.grid(row=15, column=0, sticky="ew", padx=14, pady=(14, 6))

        self.footer = ctk.CTkLabel(
            self.sidebar,
            text=f"{APP_NAME} v{APP_VERSION}",
            text_color=self.colors["text_dim"],
            font=ctk.CTkFont(size=12)
        )
        self.footer.grid(row=21, column=0, sticky="sw", padx=18, pady=18)

    def build_topbar(self):
        self.topbar = ctk.CTkFrame(self.main, fg_color=self.colors["topbar"], height=74, corner_radius=18)
        self.topbar.grid(row=0, column=0, sticky="ew", padx=18, pady=(18, 10))
        self.topbar.grid_columnconfigure(0, weight=1)

        title_wrap = ctk.CTkFrame(self.topbar, fg_color="transparent")
        title_wrap.grid(row=0, column=0, sticky="w", padx=20, pady=18)

        if self.ui_icon:
            self.topbar_icon_label = ctk.CTkLabel(title_wrap, text="", image=self.ui_icon)
            self.topbar_icon_label.pack(side="left", padx=(0, 10))

        self.page_title = ctk.CTkLabel(
            title_wrap,
            text="",
            font=ctk.CTkFont(size=25, weight="bold"),
            text_color=self.colors["text"]
        )
        self.page_title.pack(side="left")

        controls = ctk.CTkFrame(self.topbar, fg_color="transparent")
        controls.grid(row=0, column=1, sticky="e", padx=16)

        self.lang_option = ctk.CTkOptionMenu(
            controls,
            values=list(LANG_DATA.keys()),
            variable=self.language_var,
            command=self.change_language,
            width=150,
            fg_color=self.colors["card_2"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"]
        )
        self.lang_option.grid(row=0, column=0, padx=6)

        self.ver_option = ctk.CTkOptionMenu(
            controls,
            values=self.mc_versions,
            variable=self.mc_version_var,
            command=lambda _=None: self.generate_script(),
            width=130,
            fg_color=self.colors["card_2"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"]
        )
        self.ver_option.grid(row=0, column=1, padx=6)

        self.theme_segment = ctk.CTkSegmentedButton(
            controls,
            values=["Dark", "Light"],
            variable=self.theme_var,
            command=self.change_theme,
            selected_color=self.colors["accent"],
            selected_hover_color=self.colors["accent_hover"],
            unselected_color=self.colors["card_2"],
            unselected_hover_color=self.colors["nav_hover"],
            text_color=self.colors["text"],
            width=150
        )
        self.theme_segment.grid(row=0, column=2, padx=6)
        self.theme_segment.set(self.current_theme)

    def build_content(self):
        self.content = ctk.CTkFrame(self.main, fg_color="transparent")
        self.content.grid(row=1, column=0, sticky="nsew", padx=18, pady=(0, 18))
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.page_container = ctk.CTkFrame(self.content, fg_color="transparent")
        self.page_container.pack(fill="both", expand=True)

    def rebuild_ui(self):
        if self._theme_is_rebuilding:
            return
        self._theme_is_rebuilding = True
        try:
            self.sidebar.destroy()
            self.main.destroy()
            self.apply_theme()
            self.build_ui()
            self.switch_page(self.current_page)
            self.generate_script()
            self.setup_window_icon()
        finally:
            self._theme_is_rebuilding = False

    def switch_page(self, page):
        self.current_page = page
        self.clear_page()
        self.update_nav_styles()

        if page == "dashboard":
            self.page_title.configure(text=self.L("dashboard"))
            self.build_dashboard_page()
        elif page == "builder":
            self.page_title.configure(text=self.L("builder"))
            self.build_builder_page()
        elif page == "templates":
            self.page_title.configure(text=self.L("templates"))
            self.build_templates_page()
        elif page == "addons":
            self.page_title.configure(text=self.L("addons"))
            self.build_addons_page()
        elif page == "guide":
            self.page_title.configure(text=self.L("guide"))
            self.build_guide_page()
        elif page == "export":
            self.page_title.configure(text=self.L("export"))
            self.build_export_page()
        elif page == "settings":
            self.page_title.configure(text=self.L("settings"))
            self.build_settings_page()

    def update_nav_styles(self):
        for key, btn in self.nav_buttons.items():
            if key == self.current_page:
                btn.configure(fg_color=self.colors["nav_active"], hover_color=self.colors["nav_active"])
            else:
                btn.configure(fg_color="transparent", hover_color=self.colors["nav_hover"])

    def clear_page(self):
        for widget in self.page_container.winfo_children():
            widget.destroy()

    def styled_card(self, parent):
        return ctk.CTkFrame(
            parent,
            fg_color=self.colors["card"],
            corner_radius=18,
            border_width=1,
            border_color=self.colors["border"]
        )

    def title_label(self, parent, text):
        return ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors["text"]
        )

    def muted_label(self, parent, text, wrap=900):
        return ctk.CTkLabel(
            parent,
            text=text,
            text_color=self.colors["text_dim"],
            justify="left",
            wraplength=wrap,
            font=ctk.CTkFont(size=13)
        )

    def entry_block(self, parent, label, variable, width=380):
        wrap = ctk.CTkFrame(parent, fg_color="transparent")
        ctk.CTkLabel(wrap, text=label, text_color=self.colors["text"]).pack(anchor="w", pady=(0, 4))
        ent = ctk.CTkEntry(
            wrap,
            textvariable=variable,
            width=width,
            height=38,
            corner_radius=12,
            fg_color=self.colors["entry"],
            border_color=self.colors["border"],
            text_color=self.colors["text"]
        )
        ent.pack(fill="x")
        ent.bind("<KeyRelease>", lambda e: self.generate_script())
        return wrap

    def checkbox(self, parent, text, variable):
        return ctk.CTkCheckBox(
            parent,
            text=text,
            variable=variable,
            command=self.generate_script,
            text_color=self.colors["text"],
            border_color=self.colors["border"],
            fg_color=self.colors["accent"],
            hover_color=self.colors["accent_hover"]
        )

    def build_dashboard_page(self):
        root = ctk.CTkFrame(self.page_container, fg_color="transparent")
        root.pack(fill="both", expand=True)
        root.grid_columnconfigure((0, 1), weight=1)

        c1 = self.styled_card(root)
        c1.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self.title_label(c1, self.L("welcome")).pack(anchor="w", padx=20, pady=(18, 6))
        self.muted_label(c1, self.L("welcome_desc")).pack(anchor="w", padx=20, pady=(0, 14))
        active_addons = ", ".join([a for a, v in self.addons.items() if v.get()]) or "None"
        self.muted_label(
            c1,
            f"• {self.L('language')}: {self.language_var.get()}\n"
            f"• {self.L('theme')}: {self.theme_var.get()}\n"
            f"• {self.L('minecraft_version')}: {self.mc_version_var.get()}\n"
            f"• {self.L('active_addons')}: {active_addons}\n"
            f"• {self.L('template_count')}: {len(self.template_library)}",
            wrap=720
        ).pack(anchor="w", padx=20, pady=(0, 18))

        c2 = self.styled_card(root)
        c2.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)
        self.title_label(c2, self.L("quick_actions")).pack(anchor="w", padx=20, pady=(18, 10))
        btn_wrap = ctk.CTkFrame(c2, fg_color="transparent")
        btn_wrap.pack(anchor="w", padx=20, pady=(0, 18))

        for text, page, primary in [
            (self.L("builder"), "builder", True),
            (self.L("templates"), "templates", False),
            (self.L("guide"), "guide", False),
            (self.L("export"), "export", False),
        ]:
            ctk.CTkButton(
                btn_wrap,
                text=text,
                command=lambda p=page: self.switch_page(p),
                fg_color=self.colors["accent"] if primary else self.colors["card_2"],
                hover_color=self.colors["accent_hover"] if primary else self.colors["nav_hover"],
                text_color="white" if primary else self.colors["text"],
                corner_radius=12,
                height=40
            ).pack(anchor="w", fill="x", pady=5)

    def build_builder_page(self):
        root = ctk.CTkFrame(self.page_container, fg_color="transparent")
        root.pack(fill="both", expand=True)
        root.grid_columnconfigure(0, weight=0)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        left = self.styled_card(root)
        left.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        left.configure(width=500)

        right = self.styled_card(root)
        right.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        right.grid_rowconfigure(1, weight=1)
        right.grid_columnconfigure(0, weight=1)

        self.title_label(left, self.L("builder")).pack(anchor="w", padx=20, pady=(18, 6))
        self.muted_label(left, self.L("template_hint"), wrap=430).pack(anchor="w", padx=20, pady=(0, 12))

        top = ctk.CTkFrame(left, fg_color="transparent")
        top.pack(fill="x", padx=20, pady=(0, 8))

        self.entry_block(top, self.L("project_name"), self.project_name_var, 420).pack(fill="x", pady=(0, 10))
        self.entry_block(top, self.L("prefix"), self.prefix_var, 420).pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(top, text=self.L("script_type"), text_color=self.colors["text"]).pack(anchor="w", pady=(0, 4))
        self.script_type_option = ctk.CTkOptionMenu(
            top,
            values=[self.L(k) for k in self.script_type_values],
            variable=self.script_type_var,
            command=lambda _=None: self.on_script_type_change(),
            fg_color=self.colors["card_2"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"],
            width=420
        )
        self.script_type_option.pack(anchor="w", pady=(0, 10))

        self.dynamic_form = ctk.CTkScrollableFrame(left, fg_color="transparent", width=460, height=580)
        self.dynamic_form.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        btns = ctk.CTkFrame(left, fg_color="transparent")
        btns.pack(fill="x", padx=20, pady=(0, 18))

        ctk.CTkButton(
            btns, text=self.L("generate"), command=self.generate_script,
            fg_color=self.colors["accent"], hover_color=self.colors["accent_hover"],
            text_color="white", corner_radius=12, height=42
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            btns, text=self.L("copy"), command=self.copy_code,
            fg_color=self.colors["card_2"], hover_color=self.colors["nav_hover"],
            text_color=self.colors["text"], corner_radius=12, height=42
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            btns, text=self.L("reset"), command=self.reset_current_template,
            fg_color=self.colors["card_2"], hover_color=self.colors["nav_hover"],
            text_color=self.colors["text"], corner_radius=12, height=42
        ).pack(side="left")

        self.title_label(right, self.L("live_preview")).grid(row=0, column=0, sticky="w", padx=20, pady=(18, 10))

        self.preview_box = ctk.CTkTextbox(
            right,
            fg_color=self.colors["preview"],
            text_color=self.colors["text"],
            border_width=1,
            border_color=self.colors["border"],
            corner_radius=16,
            font=ctk.CTkFont(family="Consolas", size=14)
        )
        self.preview_box.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.preview_box.insert("1.0", self.L("preview_placeholder"))

        self.build_dynamic_fields()

    def build_dynamic_fields(self):
        for child in self.dynamic_form.winfo_children():
            child.destroy()

        key = self.get_script_key_from_display(self.script_type_var.get())

        if key == "script_command":
            self.build_command_fields()
        elif key == "script_joinquit":
            self.build_joinquit_fields()
        elif key == "script_healfeed":
            self.build_healfeed_fields()
        elif key == "script_warp":
            self.build_warp_fields()
        elif key == "script_reward":
            self.build_reward_fields()
        elif key == "script_kit":
            self.build_kit_fields()
        elif key == "script_broadcast":
            self.build_broadcast_fields()
        elif key == "script_home":
            self.build_home_fields()
        elif key == "script_gui":
            self.build_gui_fields()
        elif key == "script_ticket":
            self.build_ticket_fields()
        elif key == "script_report":
            self.build_report_fields()
        elif key == "script_money":
            self.build_money_fields()

        self.generate_script()

    def build_command_fields(self):
        self.entry_block(self.dynamic_form, self.L("command_name"), self.command_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("cooldown"), self.cooldown_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("command_aliases"), self.aliases_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("command_description"), self.command_description_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_self"), self.message_self_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_target"), self.message_target_var, 420).pack(fill="x", pady=6)
        self.checkbox(self.dynamic_form, self.L("use_target"), self.use_target_var).pack(anchor="w", pady=4)
        self.checkbox(self.dynamic_form, self.L("use_console"), self.use_console_var).pack(anchor="w", pady=4)
        self.checkbox(self.dynamic_form, self.L("world_only"), self.world_only_var).pack(anchor="w", pady=4)

    def build_joinquit_fields(self):
        self.entry_block(self.dynamic_form, self.L("join_message"), self.join_message_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("quit_message"), self.quit_message_var, 420).pack(fill="x", pady=6)

    def build_healfeed_fields(self):
        wrap = ctk.CTkFrame(self.dynamic_form, fg_color="transparent")
        ctk.CTkLabel(wrap, text=self.L("heal_mode"), text_color=self.colors["text"]).pack(anchor="w", pady=(0, 4))
        menu = ctk.CTkOptionMenu(
            wrap,
            values=[self.L("heal_mode_heal"), self.L("heal_mode_feed")],
            variable=self.heal_mode_var,
            command=lambda _=None: self.generate_script(),
            fg_color=self.colors["card_2"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"],
            width=420
        )
        menu.pack(anchor="w")
        wrap.pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("command_name"), self.command_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_self"), self.message_self_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_target"), self.message_target_var, 420).pack(fill="x", pady=6)
        self.checkbox(self.dynamic_form, self.L("use_target"), self.use_target_var).pack(anchor="w", pady=4)

    def build_warp_fields(self):
        self.entry_block(self.dynamic_form, self.L("warp_name"), self.warp_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("warp_permission"), self.warp_permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("teleport_message"), self.teleport_message_var, 420).pack(fill="x", pady=6)

    def build_reward_fields(self):
        self.entry_block(self.dynamic_form, self.L("command_name"), self.command_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("reward_item"), self.reward_item_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("reward_amount"), self.reward_amount_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("reward_message"), self.reward_message_var, 420).pack(fill="x", pady=6)

    def build_kit_fields(self):
        self.entry_block(self.dynamic_form, self.L("kit_name"), self.kit_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("kit_permission"), self.kit_permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("kit_items"), self.kit_items_var, 420).pack(fill="x", pady=6)

    def build_broadcast_fields(self):
        self.entry_block(self.dynamic_form, self.L("announcement_name"), self.announcement_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("broadcast_message"), self.broadcast_message_var, 420).pack(fill="x", pady=6)

    def build_home_fields(self):
        self.entry_block(self.dynamic_form, self.L("home_name"), self.home_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("teleport_message"), self.teleport_message_var, 420).pack(fill="x", pady=6)

    def build_gui_fields(self):
        self.entry_block(self.dynamic_form, self.L("command_name"), self.command_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("gui_title"), self.gui_title_var, 420).pack(fill="x", pady=6)

    def build_ticket_fields(self):
        self.entry_block(self.dynamic_form, self.L("ticket_name"), self.ticket_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_self"), self.message_self_var, 420).pack(fill="x", pady=6)

    def build_report_fields(self):
        self.entry_block(self.dynamic_form, self.L("report_name"), self.report_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_self"), self.message_self_var, 420).pack(fill="x", pady=6)

    def build_money_fields(self):
        self.entry_block(self.dynamic_form, self.L("command_name"), self.command_name_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("permission"), self.permission_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("money_amount"), self.money_amount_var, 420).pack(fill="x", pady=6)
        self.entry_block(self.dynamic_form, self.L("message_self"), self.message_self_var, 420).pack(fill="x", pady=6)

    def get_template_filter_values(self):
        return ["all"] + self.script_type_values

    def get_filtered_templates(self):
        search = self.template_search_var.get().strip().lower()
        filt = self.template_filter_var.get()

        results = []
        for tpl in self.template_library:
            if filt != "all" and tpl["script_key"] != filt:
                continue
            if search and search not in tpl["title"].lower():
                continue
            results.append(tpl)
        return results

    def build_templates_page(self):
        root = ctk.CTkFrame(self.page_container, fg_color="transparent")
        root.pack(fill="both", expand=True)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        top = self.styled_card(root)
        top.grid(row=0, column=0, sticky="ew", padx=0, pady=(0, 10))

        top_inner = ctk.CTkFrame(top, fg_color="transparent")
        top_inner.pack(fill="x", padx=20, pady=18)

        self.entry_block(top_inner, self.L("template_search"), self.template_search_var, 340).pack(side="left", padx=(0, 12))
        filter_values = self.get_template_filter_values()
        filter_labels = [self.L("filter_all")] + [self.L(v) for v in self.script_type_values]

        self.filter_map = dict(zip(filter_labels, filter_values))
        self.filter_reverse_map = {v: k for k, v in self.filter_map.items()}

        current_display = self.filter_reverse_map.get(self.template_filter_var.get(), self.L("filter_all"))
        self.template_filter_display_var = tk.StringVar(value=current_display)

        filter_wrap = ctk.CTkFrame(top_inner, fg_color="transparent")
        filter_wrap.pack(side="left", padx=(0, 12))
        ctk.CTkLabel(filter_wrap, text=self.L("script_type"), text_color=self.colors["text"]).pack(anchor="w", pady=(0, 4))
        filter_menu = ctk.CTkOptionMenu(
            filter_wrap,
            values=filter_labels,
            variable=self.template_filter_display_var,
            command=self.change_template_filter_display,
            fg_color=self.colors["card_2"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"],
            width=220
        )
        filter_menu.pack(anchor="w")

        count_label = ctk.CTkLabel(
            top_inner,
            text=f"{self.L('template_count')}: {len(self.get_filtered_templates())}",
            text_color=self.colors["text_dim"],
            font=ctk.CTkFont(size=13)
        )
        count_label.pack(side="right", padx=(12, 0), pady=(18, 0))

        sc = ctk.CTkScrollableFrame(root, fg_color="transparent")
        sc.grid(row=1, column=0, sticky="nsew")
        sc.grid_columnconfigure((0, 1), weight=1)

        filtered = self.get_filtered_templates()
        for i, template in enumerate(filtered):
            card = self.styled_card(sc)
            card.grid(row=i // 2, column=i % 2, sticky="nsew", padx=8, pady=8)

            self.title_label(card, template["title"]).pack(anchor="w", padx=20, pady=(18, 6))
            category_text = self.L(template["script_key"])
            self.muted_label(card, f"{self.L('template_hint')}\n{self.L('script_type')}: {category_text}", wrap=560).pack(anchor="w", padx=20, pady=(0, 12))

            ctk.CTkButton(
                card,
                text=self.L("generate"),
                command=lambda t=template: self.apply_template(t["script_key"], t["preset"]),
                fg_color=self.colors["accent"],
                hover_color=self.colors["accent_hover"],
                text_color="white",
                corner_radius=12,
                height=40
            ).pack(anchor="w", padx=20, pady=(0, 18))

    def change_template_filter_display(self, display_value):
        self.template_filter_var.set(self.filter_map.get(display_value, "all"))
        self.switch_page("templates")

    def build_addons_page(self):
        root = self.styled_card(self.page_container)
        root.pack(fill="both", expand=True)

        self.title_label(root, self.L("active_addons")).pack(anchor="w", padx=20, pady=(18, 10))
        frame = ctk.CTkFrame(root, fg_color="transparent")
        frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        for idx, addon in enumerate(self.addon_names):
            cb = self.checkbox(frame, addon, self.addons[addon])
            cb.grid(row=idx // 3, column=idx % 3, sticky="w", padx=16, pady=10)

    def build_guide_page(self):
        root = self.styled_card(self.page_container)
        root.pack(fill="both", expand=True)

        self.title_label(root, self.L("guide_title")).pack(anchor="w", padx=20, pady=(18, 10))
        box = ctk.CTkTextbox(
            root,
            fg_color=self.colors["preview"],
            text_color=self.colors["text"],
            border_color=self.colors["border"],
            border_width=1,
            corner_radius=16,
            font=ctk.CTkFont(size=14)
        )
        box.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        box.insert("1.0", self.L("guide_text"))
        box.configure(state="disabled")

    def build_export_page(self):
        root = ctk.CTkFrame(self.page_container, fg_color="transparent")
        root.pack(fill="both", expand=True)
        root.grid_columnconfigure((0, 1), weight=1)

        left = self.styled_card(root)
        left.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        self.title_label(left, self.L("export")).pack(anchor="w", padx=20, pady=(18, 10))

        for text, cmd, primary in [
            (self.L("save_sk"), self.save_sk_file, True),
            (self.L("save_project"), self.save_project_file, False),
            (self.L("load_project"), self.load_project_file, False),
            (self.L("copy"), self.copy_code, False),
        ]:
            ctk.CTkButton(
                left,
                text=text,
                command=cmd,
                fg_color=self.colors["accent"] if primary else self.colors["card_2"],
                hover_color=self.colors["accent_hover"] if primary else self.colors["nav_hover"],
                text_color="white" if primary else self.colors["text"],
                corner_radius=12,
                height=42
            ).pack(anchor="w", fill="x", padx=20, pady=6)

        right = self.styled_card(root)
        right.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)
        self.title_label(right, self.L("live_preview")).pack(anchor="w", padx=20, pady=(18, 10))
        txt = ctk.CTkTextbox(
            right,
            fg_color=self.colors["preview"],
            text_color=self.colors["text"],
            border_width=1,
            border_color=self.colors["border"],
            corner_radius=16,
            font=ctk.CTkFont(family="Consolas", size=13)
        )
        txt.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        txt.insert("1.0", self.preview_code if self.preview_code else self.L("preview_placeholder"))
        txt.configure(state="disabled")

    def build_settings_page(self):
        root = self.styled_card(self.page_container)
        root.pack(fill="both", expand=True)

        self.title_label(root, self.L("settings_title")).pack(anchor="w", padx=20, pady=(18, 10))
        self.muted_label(root, self.L("select_lang")).pack(anchor="w", padx=20, pady=(0, 6))

        lang_menu = ctk.CTkOptionMenu(
            root,
            values=list(LANG_DATA.keys()),
            variable=self.language_var,
            command=self.change_language,
            fg_color=self.colors["card_2"],
            button_color=self.colors["accent"],
            button_hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"],
            width=280
        )
        lang_menu.pack(anchor="w", padx=20, pady=(0, 16))

        self.muted_label(root, self.L("select_theme")).pack(anchor="w", padx=20, pady=(0, 6))

        theme_menu = ctk.CTkSegmentedButton(
            root,
            values=["Dark", "Light"],
            variable=self.theme_var,
            command=self.change_theme,
            selected_color=self.colors["accent"],
            selected_hover_color=self.colors["accent_hover"],
            unselected_color=self.colors["card_2"],
            unselected_hover_color=self.colors["nav_hover"],
            text_color=self.colors["text"],
            width=280
        )
        theme_menu.pack(anchor="w", padx=20, pady=(0, 16))
        theme_menu.set(self.current_theme)

    def launch_minecraft_launcher(self):
        system = platform.system()

        try:
            if system == "Windows":
                possible_paths = [
                    os.path.expandvars(r"%ProgramFiles(x86)%\Minecraft Launcher\MinecraftLauncher.exe"),
                    os.path.expandvars(r"%ProgramFiles%\Minecraft Launcher\MinecraftLauncher.exe"),
                    os.path.expandvars(r"%LocalAppData%\Programs\Minecraft Launcher\MinecraftLauncher.exe"),
                ]

                for path in possible_paths:
                    if os.path.exists(path):
                        subprocess.Popen([path], shell=False)
                        return

                subprocess.Popen(["cmd", "/c", "start", "", "minecraft://"], shell=False)
                return

            elif system == "Linux":
                linux_launchers = [
                    "minecraft-launcher",
                    "minecraft-launcher-beta",
                    "prismlauncher",
                    "multimc"
                ]

                for launcher in linux_launchers:
                    if shutil.which(launcher):
                        subprocess.Popen([launcher], shell=False)
                        return

                if shutil.which("xdg-open"):
                    subprocess.Popen(["xdg-open", "minecraft://"], shell=False)
                    return

                messagebox.showerror(
                    self.L("error"),
                    "Na Linuxu nebyl nalezen Minecraft launcher ani xdg-open."
                )
                return

            elif system == "Darwin":
                if shutil.which("open"):
                    subprocess.Popen(["open", "minecraft://"], shell=False)
                    return

                messagebox.showerror(self.L("error"), "Na macOS nebyl nalezen příkaz open.")
                return

            else:
                messagebox.showerror(self.L("error"), f"Nepodporovaný systém: {system}")

        except Exception as e:
            messagebox.showerror(self.L("error"), str(e))

    def change_language(self, choice):
        self.lang_name = choice
        self.lang = LANG_DATA.get(choice, LANG_DATA["Čeština"])
        current_key = self.get_script_key_from_display(self.script_type_var.get())
        self.script_type_var.set(self.L(current_key))
        self.rebuild_ui()

    def change_theme(self, choice):
        if choice == self.current_theme:
            return
        self.current_theme = choice
        self.theme_var.set(choice)
        self.rebuild_ui()

    def get_script_key_from_display(self, value):
        for key in self.script_type_values:
            if self.L(key) == value or key == value:
                return key
        return "script_command"

    def on_script_type_change(self):
        self.build_dynamic_fields()

    def get_active_addons_header(self):
        active = [name for name, var in self.addons.items() if var.get()]
        return "# Addons: " + (", ".join(active) if active else "none")

    def generate_script(self):
        key = self.get_script_key_from_display(self.script_type_var.get())
        prefix = self.prefix_var.get().strip()
        version = self.mc_version_var.get()

        code = [
            f"# {APP_NAME} generated script",
            f"# Minecraft version: {version}",
            self.get_active_addons_header(),
            ""
        ]

        generators = {
            "script_command": self.generate_command_script,
            "script_joinquit": self.generate_joinquit_script,
            "script_healfeed": self.generate_healfeed_script,
            "script_warp": self.generate_warp_script,
            "script_reward": self.generate_reward_script,
            "script_kit": self.generate_kit_script,
            "script_broadcast": self.generate_broadcast_script,
            "script_home": self.generate_home_script,
            "script_gui": self.generate_gui_script,
            "script_ticket": self.generate_ticket_script,
            "script_report": self.generate_report_script,
            "script_money": self.generate_money_script,
        }

        code.append(generators.get(key, self.generate_command_script)(prefix))
        self.preview_code = "\n".join(code).strip() + "\n"
        self.update_preview()
        self.set_status(self.L("status_generated"))

    def generate_command_script(self, prefix):
        cmd = self.command_name_var.get().strip() or "test"
        perm = self.permission_var.get().strip() or f"hsdeveloper.{cmd}"
        cooldown = self.cooldown_var.get().strip() or "0"
        aliases = [a.strip() for a in self.aliases_var.get().split(",") if a.strip()]
        self_msg = self.message_self_var.get().strip() or "&aHotovo."
        target_msg = self.message_target_var.get().strip() or "&aHotovo."
        use_target = self.use_target_var.get()
        world_only = self.world_only_var.get()

        lines = [f"command /{cmd} [<player>]:", f"    permission: {perm}"]
        if aliases:
            lines.append(f"    aliases: {', '.join(aliases)}")
        if cooldown.isdigit() and int(cooldown) > 0:
            lines.append(f"    cooldown: {cooldown} seconds")
        lines.append("    trigger:")

        if world_only:
            lines.extend([
                "        if executor is console:",
                f"            send \"{prefix}&cTento command je jen pro hráče.\"",
                "            stop"
            ])

        if use_target:
            lines.extend([
                "        if arg-1 is set:",
                "            if arg-1 is not online:",
                f"                send \"{prefix}&cHráč není online.\" to player",
                "                stop",
                f"            send \"{prefix}{target_msg}\" to arg-1",
                f"            send \"{prefix}{self_msg}\" to player",
                "        else:",
                f"            send \"{prefix}{self_msg}\" to player"
            ])
        else:
            lines.append(f"        send \"{prefix}{self_msg}\" to player")

        return "\n".join(lines)

    def generate_joinquit_script(self, prefix):
        return "\n".join([
            "on join:",
            f"    broadcast \"{prefix}{self.join_message_var.get().strip()}\"",
            "",
            "on quit:",
            f"    broadcast \"{prefix}{self.quit_message_var.get().strip()}\""
        ])

    def generate_healfeed_script(self, prefix):
        mode = self.heal_mode_var.get()
        action = "heal" if mode in ["Heal", self.L("heal_mode_heal")] else "feed"
        cmd = self.command_name_var.get().strip() or action
        perm = self.permission_var.get().strip() or f"hsdeveloper.{action}"

        lines = [f"command /{cmd} [<player>]:", f"    permission: {perm}", "    trigger:"]
        if self.use_target_var.get():
            lines.extend([
                "        if arg-1 is set:",
                f"            {action} arg-1",
                f"            send \"{prefix}{self.message_target_var.get().strip()}\" to arg-1",
                f"            send \"{prefix}{self.message_self_var.get().strip()}\" to player",
                "        else:",
                f"            {action} player",
                f"            send \"{prefix}{self.message_self_var.get().strip()}\" to player"
            ])
        else:
            lines.extend([
                f"        {action} player",
                f"        send \"{prefix}{self.message_self_var.get().strip()}\" to player"
            ])
        return "\n".join(lines)

    def generate_warp_script(self, prefix):
        warp = self.warp_name_var.get().strip() or "spawn"
        perm = self.warp_permission_var.get().strip() or f"hsdeveloper.warp.{warp}"
        return "\n".join([
            f"command /{warp}:",
            f"    permission: {perm}",
            "    trigger:",
            f"        send \"{prefix}{self.teleport_message_var.get().strip()}\" to player",
            f"        teleport player to {{{warp}}}"
        ])

    def generate_reward_script(self, prefix):
        return "\n".join([
            f"command /{self.command_name_var.get().strip() or 'reward'}:",
            f"    permission: {self.permission_var.get().strip() or 'hsdeveloper.reward'}",
            "    trigger:",
            f"        give {self.reward_amount_var.get().strip() or '1'} of {self.reward_item_var.get().strip() or 'diamond'} to player",
            f"        send \"{prefix}{self.reward_message_var.get().strip()}\" to player"
        ])

    def generate_kit_script(self, prefix):
        items = [i.strip() for i in self.kit_items_var.get().split(",") if i.strip()]
        lines = [
            f"command /kit {self.kit_name_var.get().strip() or 'starter'}:",
            f"    permission: {self.kit_permission_var.get().strip() or 'hsdeveloper.kit'}",
            "    trigger:"
        ]
        for item in items:
            lines.append(f"        give 1 of {item} to player")
        lines.append(f"        send \"{prefix}&aKit byl vydán.\" to player")
        return "\n".join(lines)

    def generate_broadcast_script(self, prefix):
        cmd = self.announcement_name_var.get().strip() or "announce"
        perm = self.permission_var.get().strip() or "hsdeveloper.announce"
        msg = self.broadcast_message_var.get().strip() or "&6Oznámení"
        return "\n".join([
            f"command /{cmd}:",
            f"    permission: {perm}",
            "    trigger:",
            f"        broadcast \"{prefix}{msg}\""
        ])

    def generate_home_script(self, prefix):
        cmd = self.home_name_var.get().strip() or "home"
        perm = self.permission_var.get().strip() or "hsdeveloper.home"
        return "\n".join([
            f"command /{cmd}:",
            f"    permission: {perm}",
            "    trigger:",
            f"        send \"{prefix}{self.teleport_message_var.get().strip()}\" to player",
            "        teleport player to {home::%uuid of player%}"
        ])

    def generate_gui_script(self, prefix):
        cmd = self.command_name_var.get().strip() or "menu"
        perm = self.permission_var.get().strip() or "hsdeveloper.menu"
        title = self.gui_title_var.get().strip() or "&8Menu"
        return "\n".join([
            f"command /{cmd}:",
            f"    permission: {perm}",
            "    trigger:",
            f"        open chest with 3 rows named \"{title}\" to player",
            f"        format slot 11 of player with diamond named \"&aInfo\" to close then run [send \"{prefix}&aKliknul jsi na info.\" to player]",
            f"        format slot 15 of player with barrier named \"&cZavřít\" to close"
        ])

    def generate_ticket_script(self, prefix):
        cmd = self.ticket_name_var.get().strip() or "ticket"
        perm = self.permission_var.get().strip() or "hsdeveloper.ticket"
        msg = self.message_self_var.get().strip() or "&aTicket vytvořen."
        return "\n".join([
            f"command /{cmd} <text>:",
            f"    permission: {perm}",
            "    trigger:",
            f"        send \"{prefix}{msg}\" to player",
            "        broadcast \"&6[Ticket] &f%player%: %arg-1%\" to all players where [input has permission \"staff.ticket\"]"
        ])

    def generate_report_script(self, prefix):
        cmd = self.report_name_var.get().strip() or "report"
        perm = self.permission_var.get().strip() or "hsdeveloper.report"
        msg = self.message_self_var.get().strip() or "&aReport odeslán."
        return "\n".join([
            f"command /{cmd} <player> <text>:",
            f"    permission: {perm}",
            "    trigger:",
            f"        send \"{prefix}{msg}\" to player",
            "        broadcast \"&c[Report] &f%player% nahlásil %arg-1%: %arg-2%\" to all players where [input has permission \"staff.report\"]"
        ])

    def generate_money_script(self, prefix):
        cmd = self.command_name_var.get().strip() or "givemoney"
        perm = self.permission_var.get().strip() or "hsdeveloper.money"
        amount = self.money_amount_var.get().strip() or "100"
        msg = self.message_self_var.get().strip() or "&aPeníze přidány."
        return "\n".join([
            f"command /{cmd} <player>:",
            f"    permission: {perm}",
            "    trigger:",
            f"        add {amount} to {{money::%uuid of arg-1%}}",
            f"        send \"{prefix}{msg}\" to player",
            f"        send \"{prefix}&aZískal jsi {amount}.\" to arg-1"
        ])

    def update_preview(self):
        if hasattr(self, "preview_box"):
            self.preview_box.delete("1.0", "end")
            self.preview_box.insert("1.0", self.preview_code)

    def apply_template(self, script_key, preset):
        self.script_type_var.set(self.L(script_key))
        for key, value in preset.items():
            if key == "command_name":
                self.command_name_var.set(value)
            elif key == "permission":
                self.permission_var.set(value)
            elif key == "heal_mode":
                self.heal_mode_var.set(value)
            elif key == "warp_name":
                self.warp_name_var.set(value)
            elif key == "warp_permission":
                self.warp_permission_var.set(value)
            elif key == "kit_name":
                self.kit_name_var.set(value)
            elif key == "kit_permission":
                self.kit_permission_var.set(value)
            elif key == "announcement_name":
                self.announcement_name_var.set(value)
            elif key == "home_name":
                self.home_name_var.set(value)
            elif key == "ticket_name":
                self.ticket_name_var.set(value)
            elif key == "report_name":
                self.report_name_var.set(value)
            elif key == "reward_item":
                self.reward_item_var.set(value)
            elif key == "reward_amount":
                self.reward_amount_var.set(value)
            elif key == "join_message":
                self.join_message_var.set(value)
            elif key == "quit_message":
                self.quit_message_var.set(value)
            elif key == "broadcast_message":
                self.broadcast_message_var.set(value)
            elif key == "gui_title":
                self.gui_title_var.set(value)
            elif key == "money_amount":
                self.money_amount_var.set(value)
            elif key == "kit_items":
                self.kit_items_var.set(value)

        self.switch_page("builder")
        self.build_dynamic_fields()
        self.generate_script()

    def reset_current_template(self):
        self.prefix_var.set("&8[&2HSDeveloper&8] &f")
        self.command_name_var.set("heal")
        self.permission_var.set("hsdeveloper.heal")
        self.cooldown_var.set("0")
        self.aliases_var.set("uzdravit,hp")
        self.command_description_var.set("Uzdraví hráče")
        self.message_self_var.set("&aHotovo.")
        self.message_target_var.set("&aByl jsi ovlivněn commandem.")
        self.use_target_var.set(True)
        self.use_console_var.set(False)
        self.world_only_var.set(True)

        self.join_message_var.set("&a%player% se připojil na server.")
        self.quit_message_var.set("&c%player% opustil server.")
        self.heal_mode_var.set("Heal")
        self.warp_name_var.set("spawn")
        self.warp_permission_var.set("hsdeveloper.warp.spawn")
        self.teleport_message_var.set("&aTeleportuji tě na warp.")
        self.reward_item_var.set("diamond")
        self.reward_amount_var.set("3")
        self.reward_message_var.set("&aZískal jsi odměnu.")
        self.kit_name_var.set("starter")
        self.kit_items_var.set("stone sword,bread,torch")
        self.kit_permission_var.set("hsdeveloper.kit.starter")
        self.broadcast_message_var.set("&6Server event právě začíná!")
        self.announcement_name_var.set("announce")
        self.home_name_var.set("home")
        self.gui_title_var.set("&8HS Menu")
        self.ticket_name_var.set("ticket")
        self.report_name_var.set("report")
        self.money_amount_var.set("100")

        self.build_dynamic_fields()
        self.generate_script()
        self.set_status(self.L("status_reset"))

    def collect_project_data(self):
        return {
            "project_name": self.project_name_var.get(),
            "language": self.language_var.get(),
            "theme": self.theme_var.get(),
            "mc_version": self.mc_version_var.get(),
            "script_type_key": self.get_script_key_from_display(self.script_type_var.get()),
            "prefix": self.prefix_var.get(),
            "command_name": self.command_name_var.get(),
            "permission": self.permission_var.get(),
            "cooldown": self.cooldown_var.get(),
            "aliases": self.aliases_var.get(),
            "command_description": self.command_description_var.get(),
            "message_self": self.message_self_var.get(),
            "message_target": self.message_target_var.get(),
            "use_target": self.use_target_var.get(),
            "use_console": self.use_console_var.get(),
            "world_only": self.world_only_var.get(),
            "join_message": self.join_message_var.get(),
            "quit_message": self.quit_message_var.get(),
            "heal_mode": self.heal_mode_var.get(),
            "warp_name": self.warp_name_var.get(),
            "warp_permission": self.warp_permission_var.get(),
            "teleport_message": self.teleport_message_var.get(),
            "reward_item": self.reward_item_var.get(),
            "reward_amount": self.reward_amount_var.get(),
            "reward_message": self.reward_message_var.get(),
            "kit_name": self.kit_name_var.get(),
            "kit_items": self.kit_items_var.get(),
            "kit_permission": self.kit_permission_var.get(),
            "broadcast_message": self.broadcast_message_var.get(),
            "announcement_name": self.announcement_name_var.get(),
            "home_name": self.home_name_var.get(),
            "gui_title": self.gui_title_var.get(),
            "ticket_name": self.ticket_name_var.get(),
            "report_name": self.report_name_var.get(),
            "money_amount": self.money_amount_var.get(),
            "template_search": self.template_search_var.get(),
            "template_filter": self.template_filter_var.get(),
            "addons": {k: v.get() for k, v in self.addons.items()}
        }

    def apply_project_data(self, data):
        self.project_name_var.set(data.get("project_name", "MyHSProject"))
        self.language_var.set(data.get("language", "Čeština"))
        self.lang_name = self.language_var.get()
        self.lang = LANG_DATA.get(self.lang_name, LANG_DATA["Čeština"])

        self.current_theme = data.get("theme", "Dark")
        self.theme_var.set(self.current_theme)
        self.mc_version_var.set(data.get("mc_version", "1.21.8"))

        self.prefix_var.set(data.get("prefix", self.prefix_var.get()))
        self.command_name_var.set(data.get("command_name", self.command_name_var.get()))
        self.permission_var.set(data.get("permission", self.permission_var.get()))
        self.cooldown_var.set(data.get("cooldown", self.cooldown_var.get()))
        self.aliases_var.set(data.get("aliases", self.aliases_var.get()))
        self.command_description_var.set(data.get("command_description", self.command_description_var.get()))
        self.message_self_var.set(data.get("message_self", self.message_self_var.get()))
        self.message_target_var.set(data.get("message_target", self.message_target_var.get()))
        self.use_target_var.set(data.get("use_target", self.use_target_var.get()))
        self.use_console_var.set(data.get("use_console", self.use_console_var.get()))
        self.world_only_var.set(data.get("world_only", self.world_only_var.get()))
        self.join_message_var.set(data.get("join_message", self.join_message_var.get()))
        self.quit_message_var.set(data.get("quit_message", self.quit_message_var.get()))
        self.heal_mode_var.set(data.get("heal_mode", self.heal_mode_var.get()))
        self.warp_name_var.set(data.get("warp_name", self.warp_name_var.get()))
        self.warp_permission_var.set(data.get("warp_permission", self.warp_permission_var.get()))
        self.teleport_message_var.set(data.get("teleport_message", self.teleport_message_var.get()))
        self.reward_item_var.set(data.get("reward_item", self.reward_item_var.get()))
        self.reward_amount_var.set(data.get("reward_amount", self.reward_amount_var.get()))
        self.reward_message_var.set(data.get("reward_message", self.reward_message_var.get()))
        self.kit_name_var.set(data.get("kit_name", self.kit_name_var.get()))
        self.kit_items_var.set(data.get("kit_items", self.kit_items_var.get()))
        self.kit_permission_var.set(data.get("kit_permission", self.kit_permission_var.get()))
        self.broadcast_message_var.set(data.get("broadcast_message", self.broadcast_message_var.get()))
        self.announcement_name_var.set(data.get("announcement_name", self.announcement_name_var.get()))
        self.home_name_var.set(data.get("home_name", self.home_name_var.get()))
        self.gui_title_var.set(data.get("gui_title", self.gui_title_var.get()))
        self.ticket_name_var.set(data.get("ticket_name", self.ticket_name_var.get()))
        self.report_name_var.set(data.get("report_name", self.report_name_var.get()))
        self.money_amount_var.set(data.get("money_amount", self.money_amount_var.get()))
        self.template_search_var.set(data.get("template_search", ""))
        self.template_filter_var.set(data.get("template_filter", "all"))

        for addon, value in data.get("addons", {}).items():
            if addon in self.addons:
                self.addons[addon].set(value)

        key = data.get("script_type_key", "script_command")
        self.script_type_var.set(self.L(key))

        self.rebuild_ui()
        self.set_status(self.L("status_loaded"))

    def copy_code(self):
        if not self.preview_code.strip():
            messagebox.showerror(self.L("error"), self.L("nothing_to_save"))
            return
        self.clipboard_clear()
        self.clipboard_append(self.preview_code)
        messagebox.showinfo(self.L("success"), self.L("copied"))

    def save_sk_file(self):
        if not self.preview_code.strip():
            messagebox.showerror(self.L("error"), self.L("nothing_to_save"))
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".sk",
            filetypes=[("Skript files", "*.sk"), ("All files", "*.*")],
            initialfile=f"{self.project_name_var.get().strip() or 'script'}.sk"
        )
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.preview_code)
        messagebox.showinfo(self.L("success"), self.L("file_saved"))
        self.set_status(self.L("status_exported"))

    def save_project_file(self):
        data = self.collect_project_data()
        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile=f"{self.project_name_var.get().strip() or 'project'}.json"
        )
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        messagebox.showinfo(self.L("success"), self.L("project_saved"))
        self.set_status(self.L("status_saved"))

    def load_project_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.apply_project_data(data)
            messagebox.showinfo(self.L("success"), self.L("project_loaded"))
        except Exception as e:
            messagebox.showerror(self.L("error"), str(e))

    def set_status(self, text):
        if hasattr(self, "logo_sub"):
            self.logo_sub.configure(text=f"Minecraft Skript Studio • {text}")


if __name__ == "__main__":
    app = HSDeveloper()
    app.mainloop()