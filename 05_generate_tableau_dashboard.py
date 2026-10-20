"""
=============================================================================
E-Commerce Customer Churn & Retention Analytics
Script 05: Tableau Dashboard Generator (.twb & .twbx)
Author: Dona Abraham (Roll No: 2501722037003)
Environment: Spyder 6 / Python 3.11+
=============================================================================
This script programmatically generates:
1. Customer_Churn_Tableau_Dashboard.twb  (Tableau Workbook)
2. Customer_Churn_Tableau_Dashboard.twbx (Packaged Tableau Workbook with embedded data)

Both files adhere strictly to the Tableau 2026.2 XML Schema & DTD specification:
- Embedded mandatory `<style />` element in all worksheet tables
- Sheet UUIDs via `<simple-id>` elements
- Structured dashboard zones, datasources, devicelayouts, and window specs
=============================================================================
"""

import os
import zipfile
import uuid

# Define script directory and dataset path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)

# Look for CSV either in current folder or parent DAV folder
csv_filename = "ecommerce_customer_churn.csv"
if os.path.exists(os.path.join(SCRIPT_DIR, csv_filename)):
    csv_dir = SCRIPT_DIR
else:
    csv_dir = PARENT_DIR

csv_full_path = os.path.join(csv_dir, csv_filename)

def build_twb_xml(is_packaged=False):
    dir_path = "Data" if is_packaged else csv_dir.replace("\\", "/")

    u_kpi = "{A1B2C3D4-E5F6-4A5B-8C9D-0E1F2A3B4C5D}"
    u_pie = "{B2C3D4E5-F6A7-4B5C-9D0E-1F2A3B4C5D6E}"
    u_pay = "{C3D4E5F6-A7B8-4C5D-0E1F-2A3B4C5D6E7F}"
    u_sat = "{D4E5F6A7-B8C9-4D5E-1F2A-3B4C5D6E7F80}"
    u_ten = "{E5F6A7B8-C9D0-4E5F-2A3B-4C5D6E7F8091}"
    u_dash = "{F6A7B8C9-D0E1-4F5A-3B4C-5D6E7F8091A2}"

    u_w_kpi = "{11111111-2222-3333-4444-555555555551}"
    u_w_pie = "{11111111-2222-3333-4444-555555555552}"
    u_w_pay = "{11111111-2222-3333-4444-555555555553}"
    u_w_sat = "{11111111-2222-3333-4444-555555555554}"
    u_w_ten = "{11111111-2222-3333-4444-555555555555}"
    u_w_dash = "{11111111-2222-3333-4444-555555555556}"

    xml = f"""<?xml version='1.0' encoding='utf-8' ?>
<workbook source-build='2026.2.0' source-platform='win' version='18.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <document-format-change-manifest>
    <AutoCreateAndUpdateDSDPhoneLayouts />
    <SetMembershipControl />
    <SheetIdentifierTracking />
    <WindowsPersistSimpleIdentifiers />
  </document-format-change-manifest>
  <preferences>
    <preference name='ui.encoding.shelf.height' value='24' />
    <preference name='ui.shelf.height' value='26' />
  </preferences>
  <datasources>
    <datasource caption='ecommerce_customer_churn' inline='true' name='federated.customer_churn' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='ecommerce_customer_churn' name='textscan.churn'>
            <connection class='textscan' directory='{dir_path}' filename='{csv_filename}' />
          </named-connection>
        </named-connections>
        <relation connection='textscan.churn' name='ecommerce_customer_churn.csv' table='[ecommerce_customer_churn#csv]' type='table'>
          <columns character-set='UTF-8' header='yes' locale='en_US' separator=','>
            <column datatype='string' name='CustomerID' ordinal='0' />
            <column datatype='integer' name='Age' ordinal='1' />
            <column datatype='string' name='Gender' ordinal='2' />
            <column datatype='string' name='CityTier' ordinal='3' />
            <column datatype='string' name='Membership' ordinal='4' />
            <column datatype='real' name='Tenure' ordinal='5' />
            <column datatype='string' name='PreferredPaymentMode' ordinal='6' />
            <column datatype='integer' name='OrderCount' ordinal='7' />
            <column datatype='real' name='CashbackAmount' ordinal='8' />
            <column datatype='integer' name='SatisfactionScore' ordinal='9' />
            <column datatype='integer' name='Churn' ordinal='10' />
          </columns>
        </relation>
        <metadata-records>
          <metadata-record class='column'>
            <remote-name>CustomerID</remote-name>
            <remote-type>129</remote-type>
            <local-name>[CustomerID]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>CustomerID</remote-alias>
            <ordinal>0</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Age</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Age]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>Age</remote-alias>
            <ordinal>1</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Gender</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Gender]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>Gender</remote-alias>
            <ordinal>2</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>CityTier</remote-name>
            <remote-type>129</remote-type>
            <local-name>[CityTier]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>CityTier</remote-alias>
            <ordinal>3</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Membership</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Membership]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>Membership</remote-alias>
            <ordinal>4</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Tenure</remote-name>
            <remote-type>5</remote-type>
            <local-name>[Tenure]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>Tenure</remote-alias>
            <ordinal>5</ordinal>
            <local-type>real</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>PreferredPaymentMode</remote-name>
            <remote-type>129</remote-type>
            <local-name>[PreferredPaymentMode]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>PreferredPaymentMode</remote-alias>
            <ordinal>6</ordinal>
            <local-type>string</local-type>
            <aggregation>Count</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>OrderCount</remote-name>
            <remote-type>20</remote-type>
            <local-name>[OrderCount]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>OrderCount</remote-alias>
            <ordinal>7</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>CashbackAmount</remote-name>
            <remote-type>5</remote-type>
            <local-name>[CashbackAmount]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>CashbackAmount</remote-alias>
            <ordinal>8</ordinal>
            <local-type>real</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>SatisfactionScore</remote-name>
            <remote-type>20</remote-type>
            <local-name>[SatisfactionScore]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>SatisfactionScore</remote-alias>
            <ordinal>9</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Churn</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Churn]</local-name>
            <parent-name>[ecommerce_customer_churn.csv]</parent-name>
            <remote-alias>Churn</remote-alias>
            <ordinal>10</ordinal>
            <local-type>integer</local-type>
            <aggregation>Sum</aggregation>
            <contains-null>true</contains-null>
          </metadata-record>
        </metadata-records>
      </connection>
      <aliases enabled='yes' />
      <column caption='Customer Status' datatype='string' name='[Calculation_Status]' role='dimension' type='nominal'>
        <calculation class='tableau' formula='IF [Churn] = 1 THEN &quot;Churned&quot; ELSE &quot;Retained&quot; END' />
      </column>
      <column caption='Churn Rate' datatype='real' default-format='p0.0%' name='[Calculation_ChurnRate]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='SUM([Churn]) / COUNT([CustomerID])' />
      </column>
      <column caption='Total Customers' datatype='integer' default-format='#,##0' name='[Calculation_TotalCust]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='COUNT([CustomerID])' />
      </column>
      <column caption='Retained Customers' datatype='integer' default-format='#,##0' name='[Calculation_Retained]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='COUNT([CustomerID]) - SUM([Churn])' />
      </column>
      <column caption='Churned Customers' datatype='integer' default-format='#,##0' name='[Calculation_Churned]' role='measure' type='quantitative'>
        <calculation class='tableau' formula='SUM([Churn])' />
      </column>
      <column datatype='real' default-format='c&quot;$&quot;#,##0.00' name='[CashbackAmount]' role='measure' type='quantitative' />
      <column datatype='integer' name='[Churn]' role='measure' type='quantitative' />
      <column datatype='string' name='[CustomerID]' role='dimension' type='nominal' />
      <column datatype='real' name='[Tenure]' role='measure' type='quantitative' />
      <column datatype='integer' name='[SatisfactionScore]' role='dimension' type='ordinal' />
      <column datatype='string' name='[PreferredPaymentMode]' role='dimension' type='nominal' />
      <column datatype='string' name='[Gender]' role='dimension' type='nominal' />
      <column datatype='string' name='[CityTier]' role='dimension' type='nominal' />
      <column datatype='string' name='[Membership]' role='dimension' type='nominal' />
      <layout dim-ordering='alphabetic' dim-percentage='0.5' measure-ordering='alphabetic' measure-percentage='0.5' show-structure='true' />
      <semantic-values>
        <semantic-value key='[Country].[Name]' value='&quot;United States&quot;' />
      </semantic-values>
    </datasource>
  </datasources>

  <worksheets>
    <!-- 1. KPI Summary Cards -->
    <worksheet name='KPI Summary'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.customer_churn' />
          </datasources>
          <datasource-dependencies datasource='federated.customer_churn'>
            <column datatype='string' name='[CustomerID]' role='dimension' type='nominal' />
            <column datatype='integer' name='[Churn]' role='measure' type='quantitative' />
            <column caption='Total Customers' datatype='integer' name='[Calculation_TotalCust]' role='measure' type='quantitative' />
            <column caption='Retained Customers' datatype='integer' name='[Calculation_Retained]' role='measure' type='quantitative' />
            <column caption='Churned Customers' datatype='integer' name='[Calculation_Churned]' role='measure' type='quantitative' />
            <column caption='Churn Rate' datatype='real' default-format='p0.0%' name='[Calculation_ChurnRate]' role='measure' type='quantitative' />
            <column-instance column='[Calculation_TotalCust]' derivation='User' name='[usr:Calculation_TotalCust:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Calculation_Retained]' derivation='User' name='[usr:Calculation_Retained:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Calculation_Churned]' derivation='User' name='[usr:Calculation_Churned:qk]' pivot='key' type='quantitative' />
            <column-instance column='[Calculation_ChurnRate]' derivation='User' name='[usr:Calculation_ChurnRate:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Text' />
            <encodings>
              <text column='[Multiple Values]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.customer_churn].[:Measure Names]</rows>
        <cols />
      </table>
      <simple-id uuid='{u_kpi}' />
    </worksheet>

    <!-- 2. Customer Retention vs Churn (Pie Chart) -->
    <worksheet name='Customer Retention Pie'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.customer_churn' />
          </datasources>
          <datasource-dependencies datasource='federated.customer_churn'>
            <column caption='Customer Status' datatype='string' name='[Calculation_Status]' role='dimension' type='nominal' />
            <column datatype='string' name='[CustomerID]' role='dimension' type='nominal' />
            <column-instance column='[Calculation_Status]' derivation='None' name='[none:Calculation_Status:nk]' pivot='key' type='nominal' />
            <column-instance column='[CustomerID]' derivation='Count' name='[cnt:CustomerID:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Pie' />
            <encodings>
              <color column='[federated.customer_churn].[none:Calculation_Status:nk]' />
              <wedge-size column='[federated.customer_churn].[cnt:CustomerID:qk]' />
              <text column='[federated.customer_churn].[none:Calculation_Status:nk]' />
              <text column='[federated.customer_churn].[cnt:CustomerID:qk]' />
            </encodings>
          </pane>
        </panes>
        <rows />
        <cols />
      </table>
      <simple-id uuid='{u_pie}' />
    </worksheet>

    <!-- 3. Churn Rate by Preferred Payment Mode -->
    <worksheet name='Churn by Payment Mode'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.customer_churn' />
          </datasources>
          <datasource-dependencies datasource='federated.customer_churn'>
            <column datatype='string' name='[PreferredPaymentMode]' role='dimension' type='nominal' />
            <column caption='Churn Rate' datatype='real' default-format='p0.0%' name='[Calculation_ChurnRate]' role='measure' type='quantitative' />
            <column-instance column='[PreferredPaymentMode]' derivation='None' name='[none:PreferredPaymentMode:nk]' pivot='key' type='nominal' />
            <column-instance column='[Calculation_ChurnRate]' derivation='User' name='[usr:Calculation_ChurnRate:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
            <encodings>
              <color column='[federated.customer_churn].[usr:Calculation_ChurnRate:qk]' />
              <text column='[federated.customer_churn].[usr:Calculation_ChurnRate:qk]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.customer_churn].[usr:Calculation_ChurnRate:qk]</rows>
        <cols>[federated.customer_churn].[none:PreferredPaymentMode:nk]</cols>
      </table>
      <simple-id uuid='{u_pay}' />
    </worksheet>

    <!-- 4. Churn Rate by Customer Satisfaction Score -->
    <worksheet name='Churn by Satisfaction'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.customer_churn' />
          </datasources>
          <datasource-dependencies datasource='federated.customer_churn'>
            <column datatype='integer' name='[SatisfactionScore]' role='dimension' type='ordinal' />
            <column caption='Churn Rate' datatype='real' default-format='p0.0%' name='[Calculation_ChurnRate]' role='measure' type='quantitative' />
            <column-instance column='[SatisfactionScore]' derivation='None' name='[none:SatisfactionScore:ok]' pivot='key' type='ordinal' />
            <column-instance column='[Calculation_ChurnRate]' derivation='User' name='[usr:Calculation_ChurnRate:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
            <encodings>
              <color column='[federated.customer_churn].[usr:Calculation_ChurnRate:qk]' />
              <text column='[federated.customer_churn].[usr:Calculation_ChurnRate:qk]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.customer_churn].[usr:Calculation_ChurnRate:qk]</rows>
        <cols>[federated.customer_churn].[none:SatisfactionScore:ok]</cols>
      </table>
      <simple-id uuid='{u_sat}' />
    </worksheet>

    <!-- 5. Average Tenure by Customer Status -->
    <worksheet name='Tenure by Status'>
      <table>
        <view>
          <datasources>
            <datasource name='federated.customer_churn' />
          </datasources>
          <datasource-dependencies datasource='federated.customer_churn'>
            <column caption='Customer Status' datatype='string' name='[Calculation_Status]' role='dimension' type='nominal' />
            <column datatype='real' name='[Tenure]' role='measure' type='quantitative' />
            <column-instance column='[Calculation_Status]' derivation='None' name='[none:Calculation_Status:nk]' pivot='key' type='nominal' />
            <column-instance column='[Tenure]' derivation='Avg' name='[avg:Tenure:qk]' pivot='key' type='quantitative' />
          </datasource-dependencies>
          <aggregation value='true' />
        </view>
        <style />
        <panes>
          <pane selection-relaxation-option='selection-relaxation-allow'>
            <view>
              <breakdown value='auto' />
            </view>
            <mark class='Bar' />
            <encodings>
              <color column='[federated.customer_churn].[none:Calculation_Status:nk]' />
              <text column='[federated.customer_churn].[avg:Tenure:qk]' />
            </encodings>
          </pane>
        </panes>
        <rows>[federated.customer_churn].[avg:Tenure:qk]</rows>
        <cols>[federated.customer_churn].[none:Calculation_Status:nk]</cols>
      </table>
      <simple-id uuid='{u_ten}' />
    </worksheet>
  </worksheets>

  <dashboards>
    <dashboard name='Customer Churn &amp; Retention Dashboard'>
      <style />
      <size maxheight='900' maxwidth='1400' minheight='900' minwidth='1400' />
      <datasources>
        <datasource caption='ecommerce_customer_churn' name='federated.customer_churn' />
      </datasources>
      <datasource-dependencies datasource='federated.customer_churn'>
        <column caption='Customer Status' datatype='string' name='[Calculation_Status]' role='dimension' type='nominal' />
        <column caption='Churn Rate' datatype='real' default-format='p0.0%' name='[Calculation_ChurnRate]' role='measure' type='quantitative' />
        <column caption='Total Customers' datatype='integer' default-format='#,##0' name='[Calculation_TotalCust]' role='measure' type='quantitative' />
        <column caption='Retained Customers' datatype='integer' default-format='#,##0' name='[Calculation_Retained]' role='measure' type='quantitative' />
        <column caption='Churned Customers' datatype='integer' default-format='#,##0' name='[Calculation_Churned]' role='measure' type='quantitative' />
        <column datatype='string' name='[CustomerID]' role='dimension' type='nominal' />
        <column datatype='real' name='[Tenure]' role='measure' type='quantitative' />
        <column datatype='integer' name='[SatisfactionScore]' role='dimension' type='ordinal' />
        <column datatype='string' name='[PreferredPaymentMode]' role='dimension' type='nominal' />
      </datasource-dependencies>
      <zones>
        <zone h='100000' id='1' type='layout-basic' w='100000' x='0' y='0'>
          
          <!-- Title Banner -->
          <zone h='9000' id='2' type='text' w='100000' x='0' y='0'>
            <formatted-text>
              <run fontalignment='1' fontcolor='#0e1a77' fontname='Segoe UI' fontsize='22' bold='true'>Tableau Customer Churn &amp; Retention Dashboard</run>
            </formatted-text>
            <zone-style>
              <format attr='border-color' value='#d0d7de' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
              <format attr='background-color' value='#f6f8fa' />
            </zone-style>
          </zone>

          <!-- KPI Cards Strip -->
          <zone h='16000' id='3' name='KPI Summary' type='worksheet' w='100000' x='0' y='9000'>
            <zone-style>
              <format attr='border-color' value='#e1e4e8' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
            </zone-style>
          </zone>

          <!-- Middle Row: Left Pie (38%), Middle Payment Bar (38%), Right Filters (24%) -->
          <zone h='37000' id='4' name='Customer Retention Pie' type='worksheet' w='38000' x='0' y='25000'>
            <zone-style>
              <format attr='border-color' value='#e1e4e8' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
            </zone-style>
          </zone>

          <zone h='37000' id='5' name='Churn by Payment Mode' type='worksheet' w='38000' x='38000' y='25000'>
            <zone-style>
              <format attr='border-color' value='#e1e4e8' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
            </zone-style>
          </zone>

          <!-- Filters Sidebar Container -->
          <zone h='75000' id='6' param='vert' type='layout-flow' w='24000' x='76000' y='25000'>
            <zone-style>
              <format attr='border-color' value='#d0d7de' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
              <format attr='background-color' value='#fbfcff' />
              <format attr='margin' value='8' />
            </zone-style>
          </zone>

          <!-- Bottom Row: Satisfaction Bar (38%), Tenure Bar (38%) -->
          <zone h='38000' id='7' name='Churn by Satisfaction' type='worksheet' w='38000' x='0' y='62000'>
            <zone-style>
              <format attr='border-color' value='#e1e4e8' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
            </zone-style>
          </zone>

          <zone h='38000' id='8' name='Tenure by Status' type='worksheet' w='38000' x='38000' y='62000'>
            <zone-style>
              <format attr='border-color' value='#e1e4e8' />
              <format attr='border-style' value='solid' />
              <format attr='border-width' value='1' />
            </zone-style>
          </zone>

        </zone>
      </zones>
      <devicelayouts>
        <devicelayout auto-generated='true' name='Phone'>
          <size maxheight='700' minheight='700' sizing-mode='vscroll' />
          <zones>
            <zone h='100000' id='20' type='layout-basic' w='100000' x='0' y='0' />
          </zones>
        </devicelayout>
      </devicelayouts>
      <simple-id uuid='{u_dash}' />
    </dashboard>
  </dashboards>

  <windows>
    <window class='worksheet' name='KPI Summary'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{u_w_kpi}' />
    </window>
    <window class='worksheet' name='Customer Retention Pie'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{u_w_pie}' />
    </window>
    <window class='worksheet' name='Churn by Payment Mode'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{u_w_pay}' />
    </window>
    <window class='worksheet' name='Churn by Satisfaction'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{u_w_sat}' />
    </window>
    <window class='worksheet' name='Tenure by Status'>
      <cards>
        <edge name='left'>
          <strip size='160'>
            <card type='pages' />
            <card type='filters' />
            <card type='marks' />
          </strip>
        </edge>
      </cards>
      <simple-id uuid='{u_w_ten}' />
    </window>
    <window class='dashboard' maximized='true' name='Customer Churn &amp; Retention Dashboard'>
      <viewpoints />
      <active id='1' />
      <simple-id uuid='{u_w_dash}' />
    </window>
  </windows>
</workbook>
"""
    return xml

def generate_tableau_files(output_dir=None):
    if output_dir is None:
        output_dir = PARENT_DIR

    twb_path = os.path.join(output_dir, "Customer_Churn_Tableau_Dashboard.twb")
    with open(twb_path, "w", encoding="utf-8") as f:
        f.write(build_twb_xml(is_packaged=False))
    print(f"[SUCCESS] Created {twb_path} ({os.path.getsize(twb_path):,} bytes)")

    twbx_path = os.path.join(output_dir, "Customer_Churn_Tableau_Dashboard.twbx")
    with zipfile.ZipFile(twbx_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("Customer_Churn_Tableau_Dashboard.twb", build_twb_xml(is_packaged=True))
        z.write(csv_full_path, arcname=f"Data/{csv_filename}")
    print(f"[SUCCESS] Created {twbx_path} ({os.path.getsize(twbx_path):,} bytes)")

if __name__ == "__main__":
    print("Generating Tableau Workbook (.twb) and Packaged Workbook (.twbx)...")
    generate_tableau_files()
