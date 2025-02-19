from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
import time
import copy


class PerformModule:

    @staticmethod
    def register(api):
        api.add_module("perform", PerformModule)

    @staticmethod
    async def navigate(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'navigate: {step["args"]["url"]}')

        if step["args"]["url"] == "${state.server}":
            step["args"]["url"] = api.state["server"]

        await api.call("selenium", "goto", step["args"], ctx, process, item)

    @staticmethod
    async def close_window(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'close_window')
        await api.call("selenium", "close_driver", step, ctx, process, item)

    @staticmethod
    async def refresh(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'refresh')
        driver = api.variables["driver"]
        driver.refresh()

    @staticmethod
    async def click(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'click on {step["args"].get("query")}')
        args = copy.deepcopy(step["args"])
        args["action"] = "click"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def dbl_click(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'dbl_click on {step["args"].get("query")}')
        args = copy.deepcopy(step["args"])
        args["action"] = "double_click"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def context_click(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'context_click on {step["args"].get("query")}')
        args = copy.deepcopy(step["args"])
        args["action"] = "context_click"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def click_sequence(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'click_sequence')
        args = step["args"]

        sequence = args["sequence"]
        for query in sequence:
            args = copy.deepcopy(step["args"])
            args["query"] = query
            args["action"] = "click"
            api.logger.debug(f'click on {query}')
            await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def dbl_click_sequence(api, step, ctx=None, process=None, item=None):
        api.logger.debug(f'dbl_click_sequence')
        args = step["args"]

        sequence = args["sequence"]
        for query in sequence:
            args = copy.deepcopy(step["args"])
            args["query"] = query
            args["action"] = "double_click"
            api.logger.debug(f'dbl_click on {query}')
            await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def press_key(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        key_value = args["key"].upper()

        api.logger.debug(f'press_key {key_value} on {args.get("query")}')

        element = await api.call("selenium", "get", args, ctx, process, item)
        key = getattr(Keys, key_value)
        element.send_keys(key)

    @staticmethod
    async def print_screen(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["folder"] = api.variables.get("folder", "./")
        args["action"] = "print_screen"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def select_option(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "select_option"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def switch_to_window(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "switch_to_window"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def switch_to_frame(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "switch_to_frame"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def switch_to_default(api, step, ctx=None, process=None, item=None):
        if "args" in step:
            args = copy.deepcopy(step["args"])
        else:
            args = {}

        args["action"] = "switch_to_default"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def switch_to_tab(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "switch_to_tab"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def type_text(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "type_text"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def clear(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "clear"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def hover_over_element(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "hover_over_element"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def move_to(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "move_to"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def move_by(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "move_by"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def drag_and_drop(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "drag_and_drop"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def drag_and_drop_by(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "drag_and_drop_by"
        await api.call("selenium", "perform", args, ctx, process, item)

    @staticmethod
    async def drag_and_drop_by_offset(api, step, ctx=None, process=None, item=None):
        args = copy.deepcopy(step["args"])
        args["action"] = "drag_and_drop_by_offset"
        await api.call("selenium", "perform", args, ctx, process, item)
