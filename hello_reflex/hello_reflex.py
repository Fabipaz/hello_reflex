import reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index(): 
    return rx.vstack(
      rx.hstack(  
            rx.button(
                "Decrement",
                
                bg="#fef2f2",
                color="#b91c1c",
                border_radius="lg",
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                bg="#ecfdf5",
                color="#047857",
                border_radius="lg",
                on_click=State.increment,
            ),
            spacing="1em",
        ) 
    ) 
   

app = rx.App()
app.add_page(index)
app.compile()