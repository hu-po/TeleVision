from asyncio import sleep
import os

from vuer import Vuer, VuerSession
from vuer.schemas import Scene, Urdf, Movable, PointLight, AmbientLight, Hands

from stompy_poses import *


app = Vuer(
    # host="0.0.0.0",
    # cert="./cert.pem",
    # key="./key.pem",
    static_root=f"{os.path.dirname(__file__)}/urdf/stompy_stl",
)


@app.spawn(start=True)
async def main(app: VuerSession):
    # Note: you can only use `set` operator with Scene objects. This is a special operator.
    app.set @ Scene(
        rawChildren=[
            AmbientLight(intensity=1),
            Movable(PointLight(intensity=1), position=[0, 0, 2]),
            Movable(PointLight(intensity=3), position=[0, 1, 2]),
        ],
        grid=True,
        up=[0, 0, 1],
    )
    await sleep(0.1)
    app.upsert @ Hands(fps=30, stream=True, key="hands")
    await sleep(0.1)
    app.upsert @ Urdf(
        src="http://localhost:8012/static/robot.urdf",
        jointValues=DEFAULT_STANDING_POSE,
        position=[0, 0, 1],
        key="robot",
        color="red",
        # materialType="standard",
        # material={"roughness": 0.5, "metalness": 0.5, "color": "red"},
    )

    i = 0
    while True:
        await sleep(0.016)
        i += 1
