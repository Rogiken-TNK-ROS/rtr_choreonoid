import os
from cnoid.Util import *
from cnoid.Base import *
from cnoid.BodyPlugin import *

try:
    from cnoid.MulticopterPlugin import *
except:
    pass

try:
    from cnoid.AGXDynamicsPlugin import *
except:
    pass

def loadProject(
    simulatorProjects, view, task, robotProject,
    taskdir="WRS2019", modeldir="rtr_models",
    enableMulticopterSimulation = True, enableVisionSimulation = False, targetVisionSensors = ""):
    
    projectdir = os.path.join(shareDirectory, taskdir, "project")
    robotdir = os.path.join(shareDirectory, modeldir, "project")
    
    itv = ItemTreeView.instance
    pm = ProjectManager.instance

    viewProject = SubProjectItem()
    viewProject.name = "ViewProject"
    viewProject.load(os.path.join(projectdir, view + ".cnoid"))
    RootItem.instance.addChildItem(viewProject)
    # itv.expandItem(viewProject, False)

    world = WorldItem()
    world.name = "World"
    RootItem.instance.addChildItem(world)

    taskProject = SubProjectItem()
    taskProject.name = task
    taskProject.load(os.path.join(projectdir, task + ".cnoid"))
    world.addChildItem(taskProject)
    # itv.expandItem(taskProject, False)

    if not isinstance(simulatorProjects, list):
        simulatorProjects = [ simulatorProjects ]
    for project in simulatorProjects:
        pm.loadProject(os.path.join(projectdir, project + ".cnoid"), world)

    # select only the first simulator item
    selectedSimulatorItems = SimulatorItemList(itv.getSelectedItems())
    for i in range(1, len(selectedSimulatorItems)):
        itv.selectItem(selectedSimulatorItems[i], False)

    robot = pm.loadProject(os.path.join(robotdir, robotProject + ".cnoid"), world)[0]

    if enableMulticopterSimulation:
        multicopterSimulator = MulticopterSimulatorItem()
        simulators = world.getDescendantItems(SimulatorItem)
        for simulator in simulators:
            simulator.addChildItem(multicopterSimulator.duplicate())

    if enableVisionSimulation:
        visionSimulator = GLVisionSimulatorItem()
        visionSimulator.setTargetSensors(targetVisionSensors)
        visionSimulator.setBestEffortMode(True)
        simulators = world.getDescendantItems(SimulatorItem)
        for simulator in simulators:
            simulator.addChildItem(visionSimulator.duplicate())
            
    pm.setCurrentProjectName(task + "-" + robotProject)
