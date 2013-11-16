#!/usr/bin/env python

import os
import maya.mel as mel

## Add paths to startup script folder
serverPath = os.environ.get('FIN_SERVER', None)
presetsPath = serverPath + '/ma/SCRIPTS/renderPresets'

def motVec2dPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/2DMotionVector.mel" 1;' )
    mel.eval( 'rename "renderPass1" "motVec2d";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass motVec2d.owner;' )
    
def motVec3dPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/3DMotionVector.mel" 1;' )
    mel.eval( 'rename "renderPass1" "motVec3d";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass motVec3d.owner;' )
    
def ambientPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/ambient.mel" 1;' )
    mel.eval( 'rename "renderPass1" "ambient";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ambient.owner;' )

def ambientIrradiancePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/ambientIrradiance.mel" 1;' )
    mel.eval( 'rename "renderPass1" "ambientIrradiance";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ambientIrradiance.owner;' )
    
def ambientMaterialColorPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/ambientMaterialColor.mel" 1;' )
    mel.eval( 'rename "renderPass1" "ambientMaterialColor";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ambientMaterialColor.owner;' )
    
def ambOccPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/ambientOcclusion.mel" 1;' )
    mel.eval( 'rename "renderPass1" "ambOcc";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ambOcc.owner;' )
    
def beautyPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/beauty.mel" 1;' )
    mel.eval( 'rename "renderPass1" "beauty";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass beauty.owner;' )
    
def beautyNoReflectRefractPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/beautyWithoutReflectionsRefractions.mel" 1;' )
    mel.eval( 'rename "renderPass1" "beautyNoReflectRefract";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass beautyNoReflectRefract.owner;' )
    
def depthPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/cameraDepth.mel" 1;' )
    mel.eval( 'rename "renderPass1" "depth";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass depth.owner;' )
    
def depthRemapPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/cameraDepthRemapped.mel" 1;' )
    mel.eval( 'rename "renderPass1" "depthRemap";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass depthRemap.owner;' )
    
def coveragePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/coverage.mel" 1;' )
    mel.eval( 'rename "renderPass1" "coverage";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass coverage.owner;' )
    
def customColorPass(name):
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/customColor.mel" 1;' )
    mel.eval( 'rename "renderPass1" ' + name + ';')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ' + name + '.owner;' )
    
def customDepthPass(name):
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/customDepth.mel" 1;' )
    mel.eval( 'rename "renderPass1" ' + name + ';')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ' + name + '.owner;' )
    
def customLabelPass(name):
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/customLabel.mel" 1;' )
    mel.eval( 'rename "renderPass1" ' + name + ';')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ' + name + '.owner;' )
    
def customVectorPass(name):
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/customVector.mel" 1;' )
    mel.eval( 'rename "renderPass1" ' + name + ';')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ' + name + '.owner;' )
    
def diffusePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/diffuse.mel" 1;' )
    mel.eval( 'rename "renderPass1" "diffuse";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass diffuse.owner;' )
    
def diffuseMatClrPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/diffuseMaterialColor.mel" 1;' )
    mel.eval( 'rename "renderPass1" "diffuseMatClr";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass diffuseMatClr.owner;' )
    
def diffuseNoShadowPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/diffuseWithoutShadows.mel" 1;' )
    mel.eval( 'rename "renderPass1" "diffuseNoShadow";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass diffuseNoShadow.owner;' )
    
def directIrradiancePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/directIrradiance.mel" 1;' )
    mel.eval( 'rename "renderPass1" "directIrradiance";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass directIrradiance.owner;' )
    
def directIrradianceNoShadowPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/directIrradianceWithoutShadows.mel" 1;' )
    mel.eval( 'rename "renderPass1" "directIrradianceNoShadow";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass directIrradianceNoShadow.owner;' )
    
def glowSourcePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/glowSource.mel" 1;' )
    mel.eval( 'rename "renderPass1" "glowSource";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass glowSource.owner;' )
    
def incandescencePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/incandescence.mel" 1;' )
    mel.eval( 'rename "renderPass1" "incandescence";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass incandescence.owner;' )
    
def incidenceCamNormPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/incidenceCamNorm.mel" 1;' )
    mel.eval( 'rename "renderPass1" "incidenceCamNorm";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass incidenceCamNorm.owner;' )
    
def incidenceCamNormMaterialPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/incidenceCamNormMaterial.mel" 1;' )
    mel.eval( 'rename "renderPass1" "incidenceCamNormMaterial";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass incidenceCamNormMaterial.owner;' )
    
def incidenceLightNormPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/incidenceLightNorm.mel" 1;' )
    mel.eval( 'rename "renderPass1" "incidenceLightNorm";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass incidenceLightNorm.owner;' )
    
def indirectPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/indirect.mel" 1;' )
    mel.eval( 'rename "renderPass1" "indirect";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass indirect.owner;' )
    
def lightVolumePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/lightVolume.mel" 1;' )
    mel.eval( 'rename "renderPass1" "lightVolume";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass lightVolume.owner;' )
    
def mattePass(name):
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/matte.mel" 1;' )
    mel.eval( 'rename "renderPass1" "' + name + '_matte";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass ' + name + '.owner;' )
    
def normalCamPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalCam.mel" 1;' )
    mel.eval( 'rename "renderPass1" "normalCam";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalCam.owner;' )
    
def normalCamMaterialPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalCamMaterial.mel" 1;' )
    mel.eval( 'rename "renderPass1" "incidenceCamNormMaterial";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalCamMaterial.owner;' )
    
def normalized2DMotVecPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalized2DMotionVector.mel" 1;' )
    mel.eval( 'rename "renderPass1" "normalized2DMotVec";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalized2DMotVec.owner;' )
    
def normalObjPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalObj.mel" 1;' )
    mel.eval( 'rename "renderPass1" "normalObj";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalObj.owner;' )
    
def normalObjMaterialPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalObjMaterial.mel" 1;' )
    mel.eval( 'rename "renderPass1" "normalObjMaterial";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalObjMaterial.owner;' )
    
def normalWorldPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalWorld.mel" 1;' )
    mel.eval( 'rename "renderPass1" "normalWorld";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalWorld.owner;' )
    
def normalWorldMaterialPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/normalWorldMaterial.mel" 1;' )
    mel.eval( 'rename "renderPass1" "normalWorldMaterial";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass normalWorldMaterial.owner;' )
    
def objectVolumePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/objectVolume.mel" 1;' )
    mel.eval( 'rename "renderPass1" "objectVolume";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass objectVolume.owner;' )
    
def opacityPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/opacity.mel" 1;' )
    mel.eval( 'rename "renderPass1" "opacity";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass opacity.owner;' )
    
def rawShadowPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/rawShadow.mel" 1;' )
    mel.eval( 'rename "renderPass1" "rawShadow";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass rawShadow.owner;' )
    
def reflectedMaterialColorPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/reflectedMaterialColor.mel" 1;' )
    mel.eval( 'rename "renderPass1" "reflectedMaterialColor";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass reflectedMaterialColor.owner;' )
    
def reflectionPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/reflection.mel" 1;' )
    mel.eval( 'rename "renderPass1" "reflection";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass reflection.owner;' )
    
def refractionPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/refraction.mel" 1;' )
    mel.eval( 'rename "renderPass1" "reflection";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass refraction.owner;' )
    
def refractionMaterialColorPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/refractionMaterialColor.mel" 1;' )
    mel.eval( 'rename "renderPass1" "refractionMaterialColor";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass refractionMaterialColor.owner;' )
    
def scatterPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/scatter.mel" 1;' )
    mel.eval( 'rename "renderPass1" "scatter";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass scatter.owner;' )
    
def sceneVolumePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/sceneVolume.mel" 1;' )
    mel.eval( 'rename "renderPass1" "sceneVolume";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass sceneVolume.owner;' )
    
def shadowPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/shadow.mel" 1;' )
    mel.eval( 'rename "renderPass1" "shadow";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass shadow.owner;' )
    
def specularPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/specular.mel" 1;' )
    mel.eval( 'rename "renderPass1" "specular";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass specular.owner;' )
    
def specularNoShadowPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/specularWithoutShadows.mel" 1;' )
    mel.eval( 'rename "renderPass1" "specularNoShadow";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass specularNoShadow.owner;' )
    
def translucencePass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/translucence.mel" 1;' )
    mel.eval( 'rename "renderPass1" "translucence";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass translucence.owner;' )
    
def translucenceNoShadowPass():
    mel.eval( 'shadingNode -asRendering renderPass;' )
    mel.eval( 'applyAttrPreset "renderPass1" "' + presetsPath + '/translucenceWithoutShadows.mel" 1;' )
    mel.eval( 'rename "renderPass1" "translucenceNoShadow";')
    mel.eval( 'connectAttr -nextAvailable defaultRenderLayer.renderPass translucenceNoShadow.owner;' )
    

    
