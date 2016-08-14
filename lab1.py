from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from panda3d.core import Point3
from direct.interval.IntervalGlobal import *
class MyApp(ShowBase):
     option = int(raw_input("What you want your panda to do? \n 1: Rotate camera\n 2: Move panda forward\n "
                         "3: Move panda backwards\n 4: Load one more panda\n"))
     if option is 1:
          def __init__(self):
                ShowBase.__init__(self)
                # Load the environment model in egg format. it's environment.egg.
                self.environ = self.loader.loadModel("models/environment")
                # Reparent the model to render.
                self.environ.reparentTo(self.render)
                # Apply scale and position transforms on the model.
                self.environ.setScale(0.25, 0.25, 0.25)
                self.environ.setPos(-8, 42, 0)
                # Add the spinCameraTask procedure to the task manager.
                self.taskMgr.add(self.spinCameraTasks, "SpinCameraTask")
                # Add the spinCameraTask procedure to the task manager.
                self.taskMgr.add(self.spinCameraTasks, "SpinCameraTask")
                # Load and transform the panda actor.
                self.pandaActor = Actor("models/panda-model",
                {"walk": "models/panda-walk4"})
                self.pandaActor.setScale(0.005, 0.005, 0.005)
                self.pandaActor.reparentTo(self.render)
                # Loop its animation.
                self.pandaActor.loop("walk")
                # Create the four lerp intervals needed for the panda to
                # walk back and forth.
                pandaPosInterval1 = self.pandaActor.posInterval(13, Point3(0, -10, 0),
                startPos=Point3(0, 10, 0))
                pandaPosInterval2 = self.pandaActor.posInterval(13, Point3(0, 10, 0),
                startPos=Point3(0, -10, 0))
                pandaHprInterval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0),
                startHpr=Point3(0, 0, 0))
                pandaHprInterval2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0),
                startHpr=Point3(180, 0, 0))
                # Create and play the sequence that coordinates the intervals.
                self.pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1,
                pandaPosInterval2, pandaHprInterval2,
                name="pandaPace")
                self.pandaPace.loop()

          def spinCameraTasks(self, task):

            angleDegrees = task.time * 6.0
            angleRadians = angleDegrees * (pi / 180.0)
            self.camera.setPos(0 , 0.0 * cos(angleRadians), 50)
            self.camera.setHpr(angleDegrees, -90, 0)
            return Task.cont


     if option is 3:
        def __init__(self):
            ShowBase.__init__(self)  # Load the environment model in egg format. it's environment.egg.
            self.environ = self.loader.loadModel("models/environment")
            # Reparent the model to render.
            self.environ.reparentTo(self.render)
            # Apply scale and position transforms on the model.
            self.environ.setScale(0.25, 0.25, 0.25)
            self.environ.setPos(-8, 42, 0)
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
            # Load and transform the panda actor.
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005)
            self.pandaActor.reparentTo(self.render)
            # Loop its animation.
            self.pandaActor.loop("walk")
            # Create the four lerp intervals needed for the panda to
            # walk back and forth.
            pandaPosInterval1 = self.pandaActor.posInterval(13, Point3(0, 10, 0),
                                                            startPos=Point3(0, -10, 0))
            pandaPosInterval2 = self.pandaActor.posInterval(13, Point3(0, -10, 0),
                                                            startPos=Point3(0, 10, 0))
            pandaHprInterval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            # Create and play the sequence that coordinates the intervals.
            self.pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1,
                                      pandaPosInterval2, pandaHprInterval2,
                                      name="pandaPace")
            self.pandaPace.loop()

     if option is 2:
             def __init__(self):
                ShowBase.__init__(self)
                # Load the environment model in egg format. it's environment.egg.
                self.environ = self.loader.loadModel("models/environment")
                # Reparent the model to render.
                self.environ.reparentTo(self.render)
                # Apply scale and position transforms on the model.
                self.environ.setScale(0.25, 0.25, 0.25)
                self.environ.setPos(-8, 42, 0)
                # Add the spinCameraTask procedure to the task manager.
                self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
                # Add the spinCameraTask procedure to the task manager.
                self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
                # Load and transform the panda actor.
                self.pandaActor = Actor("models/panda-model",
                {"walk": "models/panda-walk4"})
                self.pandaActor.setScale(0.005, 0.005, 0.005)
                self.pandaActor.reparentTo(self.render)
                # Loop its animation.
                self.pandaActor.loop("walk")
                # Create the four lerp intervals needed for the panda to
                # walk back and forth.
                pandaPosInterval1 = self.pandaActor.posInterval(13, Point3(0, -10, 0),
                startPos=Point3(0, 10, 0))
                pandaPosInterval2 = self.pandaActor.posInterval(13, Point3(0, 10, 0),
                startPos=Point3(0, -10, 0))
                pandaHprInterval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0),
                startHpr=Point3(0, 0, 0))
                pandaHprInterval2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0),
                startHpr=Point3(180, 0, 0))
                # Create and play the sequence that coordinates the intervals.
                self.pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1,
                pandaPosInterval2, pandaHprInterval2,
                name="pandaPace")
                self.pandaPace.loop()
     if option is 4:
        def __init__(self):
                ShowBase.__init__(self)
                # Load the environment model in egg format. it's environment.egg.
                self.environ = self.loader.loadModel("models/environment")
                # Reparent the model to render.
                self.environ.reparentTo(self.render)
                # Apply scale and position transforms on the model.
                self.environ.setScale(0.25, 0.25, 0.25)
                self.environ.setPos(-8, 42, 0)
                # Add the spinCameraTask procedure to the task manager.
                self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
                # Add the spinCameraTask procedure to the task manager.
                self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
                # Load and transform the panda actor.
                self.pandaActor = Actor("models/panda-model",
                {"walk": "models/panda-walk4"})

                self.pandaActor.setScale(0.005, 0.005, 0.005)
                self.pandaActor.reparentTo(self.render)
                # Loop its animation.
                self.pandaActor.loop("walk")
                # Create the four lerp intervals needed for the panda to
                # walk back and forth.
                pandaPosInterval1 = self.pandaActor.posInterval(13, Point3(0, -10, 0),
                startPos=Point3(0, 10, 0))
                pandaPosInterval2 = self.pandaActor.posInterval(13, Point3(0, 10, 0),
                startPos=Point3(0, -10, 0))
                pandaHprInterval1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0),
                startHpr=Point3(0, 0, 0))
                pandaHprInterval2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0),
                startHpr=Point3(180, 0, 0))
                # Create and play the sequence that coordinates the intervals.
                self.pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1,
                pandaPosInterval2, pandaHprInterval2,
                name="pandaPace")
                self.pandaPace.loop()
                self.panda2Actor = Actor("models/panda-model",
                {"walk": "models/panda-walk4"})
                self.panda2Actor.setScale(0.005, 0.005, 0.005)
                self.panda2Actor.reparentTo(self.render)
                # Loop its animation.
                self.panda2Actor.loop("walk")
                                # Create the four lerp intervals needed for the panda to
                # walk back and forth.
                pandaPosiInterval1 = self.panda2Actor.posInterval(10, Point3(0, -10, 0),
                startPos=Point3(0, 10, 0))
                pandaPosiInterval2 = self.panda2Actor.posInterval(13, Point3(0, 10, 0),
                startPos=Point3(0, -10, 0))
                panda2HprInterval1 = self.panda2Actor.hprInterval(3, Point3(180, 0, 0),
                startHpr=Point3(0, 0, 0))
                panda2HprInterval2 = self.panda2Actor.hprInterval(3, Point3(0, 0, 0),
                startHpr=Point3(180, 0, 0))
                self.pandasPace = Sequence(pandaPosiInterval1, panda2HprInterval1,
                pandaPosiInterval2, panda2HprInterval2,
                name="pandasPace")
                self.pandasPace.loop()


     def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont




app = MyApp()
app.run() #enters the panda3D main loop