import reflex as rx
from pcweb.templates.docpage import docpage, h1_comp, text_comp_2


def component_card(name: str, link: str, section: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.image(
                src=rx.color_mode_cond(
                    f"/components_previews/{section.lower()}/light/{name.lower()}.svg",
                    f"/components_previews/{section.lower()}/dark/{name.lower()}.svg",
                ),
                loading="lazy",
                alt="Image preview of " + name,
                class_name="object-contain object-center h-full w-full",
            ),
            rx.box(
                rx.text(
                    name.capitalize(),
                    class_name="truncate font-base text-slate-12",
                ),
                rx.icon("chevron-right", size=14, class_name="text-slate-9"),
                class_name="bottom-0 absolute flex flex-row justify-between w-full px-4 py-2 items-center",
            ),
            class_name="rounded-xl border overflow-hidden relative box-border shadow-large bg-slate-2 hover:bg-slate-3 transition-bg border-slate-5",
        ),
        href=link,
    )


def get_component_list(component_type: str = "core"):
    from pcweb.pages.docs import component_list, graphing_components

    if component_type == "core":
        return component_list
    elif component_type == "graphing":
        return graphing_components
    else:
        raise ValueError(f"Unknown component type: {component_type}")


def create_previews(
    path: str,
    description: str,
    component_category: str,
    prefix: str = "",
    type: str = "core",
):
    @docpage(right_sidebar=False, set_path=f"/docs/library/{prefix}" + path)
    def page() -> rx.Component:
        from pcweb.components.docpage.sidebar.sidebar_items import get_component_link

        component_list = get_component_list(type)

        return rx.box(
            rx.box(
                h1_comp(text=component_category),
                text_comp_2(
                    text=description,
                ),
                class_name="flex flex-col w-full",
            ),
            rx.box(
                *[
                    component_card(
                        name=rx.utils.format.to_title_case(component[0]),
                        link=get_component_link(
                            component_category, component, prefix.strip("/")
                        ),
                        section=component_category,
                    )
                    for component in component_list[component_category]
                ],
                class_name="gap-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3",
            ),
            class_name="flex flex-col h-full mb-10",
        )

    return page


# Core Components
core_components_dict = {
    "datadisplay": {
        "path": "datadisplay",
        "description": "Tools to show information clearly. These include ways to highlight important details, show user pictures, display lists, indicate progress, and organize data neatly.",
        "component_category": "Datadisplay",
    },
    "disclosure": {
        "path": "disclosure",
        "description": "Components for revealing or hiding content, such as tabs and accordions. These are useful for creating expandable sections, organizing information, and improving user interface navigation.",
        "component_category": "Disclosure",
    },
    "dynamic_rendering": {
        "path": "dynamic-rendering",
        "description": "Components that help with dynamic rendering, such as conditional rendering and dynamic components. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "Dynamic-Rendering",
    },
    "forms": {
        "path": "forms",
        "description": "Components for collecting user input, such as text fields, checkboxes, and radio buttons. These are useful for creating interactive forms and user input.",
        "component_category": "Forms",
    },
    "html": {
        "path": "html",
        "description": "Components that help with dynamic rendering, such as conditional rendering and dynamic components. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "Html",
    },
    "layout": {
        "path": "layout",
        "description": "Components that help with layout, such as containers, grids, and spacing. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "Layout",
    },
    "media": {
        "path": "media",
        "description": "Components that help with media, such as images, videos, and audio. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "Media",
    },
    "other": {
        "path": "other",
        "description": "Miscellaneous components that don't fit into other categories, such as clipboard, script, skeleton, and theme. These components provide additional functionality and customization options for your application.",
        "component_category": "Other",
    },
    "overlays": {
        "path": "overlay",
        "description": "Components that help with overlays, such as modals, popovers, and tooltips. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "Overlay",
    },
    "typography": {
        "path": "typography",
        "description": "Components that help with typography, such as headings, paragraphs, and lists. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "Typography",
    },
    "state": {
        "path": "state",
        "description": "Components that help with state, such as state variables, state hooks, and state management. These are useful for creating responsive and interactive user interfaces.",
        "component_category": "State",
    },
}

library_previews = [
    create_previews(
        path=value["path"],
        description=value["description"],
        component_category=value["component_category"],
        type="core",
    )
    for key, value in core_components_dict.items()
]

# Graphing Components
graphing_components_dict = {
    "charts": {
        "path": "charts",
        "description": "Components for creating various types of charts and graphs. These are useful for data visualization and presenting complex information in an easily understandable format.",
        "component_category": "Charts",
    },
    "general": {
        "path": "general",
        "description": "General-purpose graphing components that provide foundational elements for creating custom visualizations. These components offer flexibility and can be combined to create more complex graphical representations.",
        "component_category": "General",
    },
    "other": {
        "path": "other",
        "description": "Other graphing components that provide additional functionality and customization options for creating custom visualizations. These components can be used to enhance the graphical representation of data and improve user experience.",
        "component_category": "Other",
    },
}

graphing_previews = [
    create_previews(
        path=value["path"],
        description=value["description"],
        component_category=value["component_category"],
        prefix="/graphing",
        type="graphing",
    )
    for key, value in graphing_components_dict.items()
]


components_previews_pages = library_previews + graphing_previews
