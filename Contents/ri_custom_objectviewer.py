# -*- coding: utf-8 -*-

"""!
Softimage like Object Viewer For Maya V 1.5
              - Set to Maya_Root after Set group is made
              - Delete unused modelPanel that this script made
@file
@author Ritaro

"""

import maya.cmds as cmds
import maya.mel as mel

first_selected_node=[]

def cam_far_slider(value,n_cam):
    n_cameraShape = cmds.listRelatives(n_cam, children=True)[0]
    cmds.setAttr( n_cameraShape + '.farClipPlane', value )
def cam_near_slider(value,n_cam):
    n_cameraShape = cmds.listRelatives(n_cam, children=True)[0]
    cmds.setAttr( n_cameraShape + '.nearClipPlane', value )

def cam_txoffset_slider(value,n_const_node):
    cmds.setAttr(n_const_node + '.target[0].targetOffsetTranslateX',value)
def cam_tyoffset_slider(value,n_const_node):
    cmds.setAttr(n_const_node + '.target[0].targetOffsetTranslateY',value)
def cam_tzoffset_slider(value,n_const_node):
    cmds.setAttr(n_const_node + '.target[0].targetOffsetTranslateZ',value)

def cam_rxoffset_slider(value,n_const_node):
    cmds.setAttr(n_const_node + '.target[0].targetOffsetRotateX',value)
def cam_ryoffset_slider(value,n_const_node):
    cmds.setAttr(n_const_node + '.target[0].targetOffsetRotateY',value)
def cam_rzoffset_slider(value,n_const_node):
    cmds.setAttr(n_const_node + '.target[0].targetOffsetRotateZ',value)

def object_view_menu(*args):
    if not cmds.ls( sl=True ):
        print 'Nothing is selected'
    else:
        first_selected_node = cmds.ls(sl=True)[0]

        cmds.select(clear=True)

        all_model_panels = cmds.getPanel(type='modelPanel')
        m_panel_list =[]
        for o_panel in all_model_panels:
            o_label = cmds.panel(o_panel, q=True, label=True)
            if "CustomObjectViewer" in o_label:
                m_panel_list.append(o_panel) 

        invis_panel_list = cmds.getPanel(invisiblePanels=True)

        for d_panel in m_panel_list:
            if d_panel in invis_panel_list:
                cmds.deleteUI(d_panel,panel=True)

        cmds.select(clear=True)
        mel.eval('CreateCameraAimUp;')
        aimup_list = cmds.ls( sl=True )
        cmds.select(clear=True)

        for n_camdata in aimup_list:
            cmds.select(n_camdata,r=True)
            n_dataShape = cmds.listRelatives(n_camdata, children=True)[0]
            n_cam_type = cmds.objectType(n_dataShape)
            if n_cam_type == 'camera':
                n_number = n_camdata[len('camera'):]
                cmds.setAttr( n_dataShape + '.nearClipPlane', 10 )
                cmds.setAttr( n_camdata + '.translateZ', 30)
                o_cam = n_camdata
            if '_aim' in n_camdata:
                cmds.setAttr( n_camdata + '.translateX', 0)
                cmds.setAttr( n_camdata + '.translateY', 0)                
                cmds.setAttr( n_camdata + '.translateZ', 0)
            cmds.select(clear=True)

        o_pregrp = cmds.listRelatives(o_cam,parent=True )[0]
        cmds.select(o_pregrp,r=True)
        o_grp = cmds.rename('ObjectViewCamera_group' + n_number )
        cmds.parent(o_grp, first_selected_node, relative=True )


        cmds.select(clear=True)
        cmds.select(o_grp,r=True)
        pre_parent = cmds.listRelatives(o_grp,parent=True )[0]
        cmds.parent(o_grp,world=True)
        const_node = cmds.parentConstraint(pre_parent,o_grp,maintainOffset=True)[0]
        cmds.select(clear=True)

        try:
            cmds.window()
            window = cmds.window('CustomObjectViewer' + n_number, 
                title='Custom ObjectViewer' + n_number, sizeable=True, 
                topLeftCorner=[200, 200], widthHeight=(400,470))
            form = cmds.formLayout()
            c_model= cmds.modelPanel(label='CustomObjectViewer_Panel' + n_number, camera=o_cam)
        except:
            print 'Check Panel Editor & CleanUp Unused Panels !!'

        cmds.setParent('..')
        column = cmds.columnLayout()
        cmds.rowLayout(numberOfColumns=2)
        cmds.floatSliderGrp(label=' Far ClipPlane ',field=True,columnWidth3=[85,40,70],
            adjustableColumn=3, minValue=0.1, maxValue=100,fieldMinValue=0.1,
            fieldMaxValue=100, value=70,
            dragCommand=lambda x:cam_far_slider(x,o_cam),
            changeCommand=lambda x:cam_far_slider(x,o_cam))
        cmds.floatSliderGrp(label='NearClipPlane ',field=True,columnWidth3=[85,40,70],
            adjustableColumn=3, minValue=0.01, maxValue=100,fieldMinValue=0.01,
            fieldMaxValue=100, value=10,
            dragCommand=lambda x:cam_near_slider(x,o_cam),
            changeCommand=lambda x:cam_near_slider(x,o_cam))
        cmds.setParent('..')

        cmds.rowLayout(numberOfColumns=3)
        cmds.floatSliderGrp(label='Trans Offset X',field=True,columnWidth3=[85,40,50],
            adjustableColumn=3, minValue=-100, maxValue=100,fieldMinValue=-100,
            fieldMaxValue=100, value=0,
            dragCommand=lambda x:cam_txoffset_slider(x,const_node),
            changeCommand=lambda x:cam_txoffset_slider(x,const_node))
        cmds.floatSliderGrp(label='Y',field=True,columnWidth3=[10,40,50],
            adjustableColumn=3, minValue=-100, maxValue=100,fieldMinValue=-100,
            fieldMaxValue=100, value=0,
            dragCommand=lambda x:cam_tyoffset_slider(x,const_node),
            changeCommand=lambda x:cam_tyoffset_slider(x,const_node))
        cmds.floatSliderGrp(label='Z',field=True,columnWidth3=[10,40,50],
            adjustableColumn=3, minValue=-100, maxValue=100,fieldMinValue=-100,
            fieldMaxValue=100, value=0,
            dragCommand=lambda x:cam_tzoffset_slider(x,const_node),
            changeCommand=lambda x:cam_tzoffset_slider(x,const_node))
        cmds.setParent('..')

        cmds.rowLayout(numberOfColumns=3)
        cmds.floatSliderGrp(label='RotateOffset X',field=True,columnWidth3=[85,40,50],
            adjustableColumn=3, minValue=0, maxValue=360,fieldMinValue=0,
            fieldMaxValue=360, value=0,
            dragCommand=lambda x:cam_rxoffset_slider(x,const_node),
            changeCommand=lambda x:cam_rxoffset_slider(x,const_node))
        cmds.floatSliderGrp(label='Y',field=True,columnWidth3=[10,40,50],
            adjustableColumn=3, minValue=0, maxValue=360,fieldMinValue=0,
            fieldMaxValue=360, value=0,
            dragCommand=lambda x:cam_ryoffset_slider(x,const_node),
            changeCommand=lambda x:cam_ryoffset_slider(x,const_node))
        cmds.floatSliderGrp(label='Z',field=True,columnWidth3=[10,40,50],
            adjustableColumn=3, minValue=0, maxValue=360,fieldMinValue=0,
            fieldMaxValue=360, value=0,
            dragCommand=lambda x:cam_rzoffset_slider(x,const_node),
            changeCommand=lambda x:cam_rzoffset_slider(x,const_node))
        cmds.setParent('..')


        cmds.formLayout(form,edit=True,
             attachForm=[
                  (c_model,'left',5),(c_model,'top',0),(c_model,'right',5),(c_model,'bottom',80),
                  (column,'left',5),(column,'top',400),(column,'right',0),(column,'bottom',0)
                  ],
             attachPosition=[(column,'right',0,100)],
             attachNone=[(column,'top')]
             )
        cmds.modelEditor(c_model,edit=True,grid=False,
            displayAppearance='smoothShaded',activeOnly=False, displayTextures=True )
        cmds.showWindow( window )

