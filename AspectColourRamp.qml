<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" maxScale="0" minScale="1e+08" version="3.20.1-Odense">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" enabled="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <Option type="Map">
      <Option name="WMSBackgroundLayer" type="bool" value="false"/>
      <Option name="WMSPublishDataSourceUrl" type="bool" value="false"/>
      <Option name="embeddedWidgets/count" type="int" value="0"/>
      <Option name="identify/format" type="QString" value="Value"/>
    </Option>
  </customproperties>
  <pipe>
    <provider>
      <resampling maxOversampling="2" enabled="false" zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour"/>
    </provider>
    <rasterrenderer alphaBand="-1" type="paletted" band="1" opacity="1" nodataColor="">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry value="0" color="#f7fbff" alpha="255" label="0"/>
        <paletteEntry value="1" color="#e2edf8" alpha="255" label="1"/>
        <paletteEntry value="2" color="#cde0f1" alpha="255" label="2"/>
        <paletteEntry value="3" color="#afd1e7" alpha="255" label="3"/>
        <paletteEntry value="4" color="#89bedc" alpha="255" label="4"/>
        <paletteEntry value="5" color="#60a6d2" alpha="255" label="5"/>
        <paletteEntry value="6" color="#3e8ec4" alpha="255" label="6"/>
        <paletteEntry value="7" color="#2272b5" alpha="255" label="7"/>
        <paletteEntry value="8" color="#0a549e" alpha="255" label="8"/>
        <paletteEntry value="9" color="#08306b" alpha="255" label="9"/>
      </colorPalette>
      <colorramp name="[source]" type="gradient">
        <Option type="Map">
          <Option name="color1" type="QString" value="247,251,255,255"/>
          <Option name="color2" type="QString" value="8,48,107,255"/>
          <Option name="discrete" type="QString" value="0"/>
          <Option name="rampType" type="QString" value="gradient"/>
          <Option name="stops" type="QString" value="0.13;222,235,247,255:0.26;198,219,239,255:0.39;158,202,225,255:0.52;107,174,214,255:0.65;66,146,198,255:0.78;33,113,181,255:0.9;8,81,156,255"/>
        </Option>
        <prop k="color1" v="247,251,255,255"/>
        <prop k="color2" v="8,48,107,255"/>
        <prop k="discrete" v="0"/>
        <prop k="rampType" v="gradient"/>
        <prop k="stops" v="0.13;222,235,247,255:0.26;198,219,239,255:0.39;158,202,225,255:0.52;107,174,214,255:0.65;66,146,198,255:0.78;33,113,181,255:0.9;8,81,156,255"/>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0" gamma="1"/>
    <huesaturation saturation="0" colorizeOn="0" grayscaleMode="0" colorizeRed="255" colorizeBlue="128" colorizeGreen="128" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
