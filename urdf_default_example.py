from asyncio import sleep
from vuer import Vuer
from vuer.schemas import Urdf, Movable, DefaultScene

app = Vuer()

pi = 3.14

@app.spawn(start=True)
async def main(app):
    app.set @ DefaultScene(
        Movable(
            Urdf(
                src="https://raw.githubusercontent.com/nasa-jpl/m2020-urdf-models/main/rover/m2020.urdf",
                jointValues={},
                rotation=[pi, 0, 0],
            ),
            position=[0, 0, 0.15],
        ),
        grid=True,
        collapseMenu=True,
    )

    while True:
        await sleep(16)