from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    SCREENWIDTH = 400
    SCREENHEIGHT = 850

    PROGRESSBAR = 30










    def shrink(e):
        mainScreen.controls[0].width = 120
        mainScreen.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        mainScreen.update()


    createTask = Container(
        content=Container(on_click=lambda _: page.go('/'),
            height=40, width=40,
            content=Text('X')
        )
    )
    

    tasks = Column(
        height=400, scroll='auto',
        # controls=[Container()]
    )

    for i in range(10):
        tasks.controls.append(
            Container(
                height=70, 
                width=400, 
                bgcolor=BG,
                border_radius=15, padding=padding.only(left=20, top=25),
                content=CustomCheckBox(color=PINK, 
                                       label='Create interesting content!'
                                       )),
        )

    categoriesCard = Row(
        scroll='auto'
    )

    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categoriesCard.controls.append(
            Container(
                bgcolor=BG, 
                height=110, 
                width=170,
                border_radius=15,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            border_radius=15,
                            bgcolor='white12',
                            padding=padding.only(right=PROGRESSBAR * i),
                            content=Container(
                                bgcolor=PINK
                            )
                        )
                    ]
                )
            )
        )


    firstPage = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                            content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATION_IMPORTANT_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height=20),
                Text(
                    value='What\'s up, Olivia!'
                ),
                Text(
                    value='CATEGORIES'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categoriesCard
                ),
                Container(height=10),
                Text("Today's Tasks"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(bottom=2, right=20,
                            icon = icons.ADD, on_click=lambda _: page.go('/create_task')
                        )
                    ],
                ),
            ]
        )
    )


    profile = Container()
    mainScreen = Row(
        controls=[
            Container(
                width=SCREENWIDTH,
                height=SCREENHEIGHT,
                bgcolor=FG,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve='decelerate'),
                border_radius=15,
                padding=padding.only(
                    top=50, left=20, right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        firstPage
                    ]
                )
            )
        ]
    )



    screen = Container(
        width=SCREENWIDTH,
        height=SCREENHEIGHT,
        bgcolor=BG,
        border_radius=15,
        content=Stack(
            controls=[
                profile,
                mainScreen,
            ]
        )
    )

    pages = {
        '/':View(
                "/",
                [
                    screen
                ],
            ),
        '/create_task':View(
                "/create_task",
                [
                    createTask
                ],
            ),
    }


    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.on_route_change = route_change
    page.go(page.route)



    page.add(screen)

    







app(target=main)