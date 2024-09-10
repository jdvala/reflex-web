import reflex as rx
from pcweb.pages.docs import getting_started
from pcweb.components.button import button
from pcweb.components.icons.icons import get_icon
from pcweb.pages.index.demos.demos import demo_section


def hero() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.el.section(
        # Headings
        rx.el.h1(
            """Build web apps in pure Python. 
An open-source framework
to ship beautiful and fast""",
            class_name="inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full font-xx-large text-balance text-center text-transparent whitespace-pre",
        ),
        # rx.el.h2(
        #     rx.el.span("An open-source framework to ship beautiful apps fast."),
        #     rx.el.span("Deploy with a single command."),
        #     class_name="flex flex-col font-md text-center text-slate-9",
        # ),
        # Buttons
        rx.box(
            rx.link(
                button(
                    "Start building",
                    class_name="!px-[1.125rem] !py-2 !h-12 !font-smbold !text-[1.125rem] !leading-[1.625rem] !tracking-[-0.01688rem] transition-bg rounded-[0.875rem]",
                ),
                underline="none",
                href=getting_started.introduction.path,
            ),
            rx.link(
                button(
                    "Get a demo",
                    variant="muted",
                    class_name="!px-[1.125ren] !py-2 !h-12 !font-semibold !text-[1.125rem] !leading-[1.625rem] !tracking-[-0.01688rem] transition-bg rounded-[0.875rem] !w-[9.3125rem]",
                ),
                href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX",
                is_external=True,
                underline="none",
            ),
            class_name="flex flex-row items-center gap-4",
        ),
        # Pip install
        rx.box(
            get_icon("copy", class_name="!text-slate-9 [&>svg]:w-4 [&>svg]:h-4"),
            rx.el.p(
                "$ pip install reflex",
                class_name="font-['JetBrains_Mono'] font-medium font-small text-[0.8125rem] text-center text-slate-9 leading-6",
            ),
            on_click=rx.set_clipboard("pip install reflex"),
            class_name="flex flex-row items-center gap-3 hover:bg-slate-3 px-3 py-2 rounded-xl cursor-pointer transition-bg",
        ),
        class_name="flex flex-col justify-center items-center gap-8 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-8 pt-24 lg:pt-48",
    )
