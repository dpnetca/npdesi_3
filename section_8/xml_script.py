#!/usr/bin/env python

from lxml import etree

if __name__ == "__main__":

    xml_as_string = """
    <ins_api>
      <type>cli_show</type>
      <version>1.2</version>
      <sid>eoc</sid>
      <outputs>
        <output>
          <body>
          <hostname>nxosv.cisco.com</hostname>
         </body>
          <input>show hostname</input>
          <msg>Success</msg>
          <code>200</code>
        </output>
      </outputs>
    </ins_api>
    """
    xml_obj = etree.fromstring(xml_as_string)
    print(xml_obj)

    data = xml_obj.find(".//hostname")
    print(data.text)

