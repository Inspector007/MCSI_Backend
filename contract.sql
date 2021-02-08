BEGIN;
--
-- Create model AdditionalCharges
--
CREATE TABLE `contract_additionalcharges` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `headerName` varchar(30) NOT NULL, `additionalCost` double precision NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model AdditionalContractField
--
CREATE TABLE `contract_additionalcontractfield` (`contractaddfieldid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(200) NULL, `cost` double precision NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model Capture_Daily_KPI
--
CREATE TABLE `contract_capture_daily_kpi` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `actualcount` integer NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model Contract
--
CREATE TABLE `contract_contract` (`contractid` varchar(50) NOT NULL PRIMARY KEY, `contractwith` varchar(5) NOT NULL, `cost` double precision NULL, `oppourtunityid` varchar(20) NULL, `betterpalcesiteid` varchar(50) NULL, `vertical` varchar(50) NULL, `bonus` integer NULL, `bonusduration` varchar(10) NOT NULL, `startdate` date NOT NULL, `enddate` date NOT NULL, `closedate` date NOT NULL, `extenddate` date NOT NULL, `approvedby` varchar(45) NULL, `approvestatus` smallint NULL, `remark` varchar(200) NULL, `address1` varchar(100) NULL, `address2` varchar(100) NULL, `city` varchar(30) NULL, `servicetype` varchar(100) NULL, `panno` varchar(10) NULL, `gstinno` varchar(15) NULL, `place_of_supply_city` varchar(30) NULL, `place_of_supply_state` varchar(30) NULL, `address_of_delivery_city` varchar(30) NULL, `address_of_delivery_state` varchar(30) NULL, `doclink1` varchar(500) NULL, `doclink2` varchar(500) NULL, `doclink3` varchar(500) NULL, `doclink4` varchar(500) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `ba_id` varchar(10) NULL);
--
-- Create model Contract_Percentage_Field
--
CREATE TABLE `contract_contract_percentage_field` (`contract_per_loc_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `state` varchar(200) NULL, `city` varchar(200) NULL, `percentage` double precision NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contract_id` varchar(50) NOT NULL);
--
-- Create model ContractDetail
--
CREATE TABLE `contract_contractdetail` (`contractdetid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `requirequantity` integer NULL, `startquantity` integer NULL, `endquantity` integer NULL, `uom` varchar(20) NULL, `upperdev` double precision NULL, `lowerdev` double precision NULL, `fixedcost` double precision NULL, `ot` double precision NULL, `adhoc` double precision NULL, `margintype` varchar(5) NULL, `marginvalue` double precision NULL, `isapplicablecomrange` smallint NULL, `billingcycle` varchar(50) NULL, `finalsubmissionflag` smallint NULL, `remark` varchar(200) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model ContractDetail_Reference_Aadharid
--
CREATE TABLE `contract_contractdetail_reference_aadharid` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `aadhaarid` longtext NOT NULL, `contractdetailid_fk_id` integer NOT NULL);
--
-- Create model ContractType
--
CREATE TABLE `contract_contracttype` (`contracttypeid` integer NOT NULL PRIMARY KEY, `cnttypename` varchar(30) NOT NULL, `cnttypecode` varchar(5) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model Designation
--
CREATE TABLE `contract_designation` (`designation_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `designation_name` varchar(30) NULL, `designation_code` varchar(5) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model DetailAttCapture
--
CREATE TABLE `contract_detailattcapture` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `date` date NOT NULL, `skillcount` integer NULL, `skillotcount` integer NULL, `extrashift` integer NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contractid_id` varchar(50) NOT NULL, `designation_id` integer NOT NULL);
--
-- Create model Document
--
CREATE TABLE `contract_document` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `description` varchar(255) NOT NULL, `document` varchar(100) NOT NULL, `document1` varchar(100) NULL, `document2` varchar(100) NULL, `uploaded_at` datetime(6) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contractid_id` varchar(50) NOT NULL UNIQUE);
--
-- Create model InvoiceDetailCapture
--
CREATE TABLE `contract_invoicedetailcapture` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `contractTypeName` varchar(50) NOT NULL, `oppourtunityId` varchar(50) NOT NULL, `location` varchar(50) NULL, `invoiceDate` date NOT NULL, `skillName` varchar(50) NOT NULL, `designation` varchar(50) NOT NULL, `attendenceCount` integer NOT NULL, `cost` double precision NOT NULL, `totalcost` double precision NOT NULL, `status` varchar(2) NOT NULL, `rowInvoiceFlag` varchar(2) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contractid_id` varchar(50) NOT NULL);
--
-- Create model InvoiceHeaderMaster
--
CREATE TABLE `contract_invoiceheadermaster` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `address` varchar(300) NOT NULL, `gst` varchar(30) NOT NULL, `cin` varchar(30) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `stateid_id` integer NOT NULL);
--
-- Create model InvoiceMaster
--
CREATE TABLE `contract_invoicemaster` (`invoiceid` varchar(50) NOT NULL PRIMARY KEY, `finaltotal` double precision NOT NULL, `selectedrowids` varchar(300) NULL, `state` varchar(70) NULL, `city` varchar(70) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contractid_id` varchar(50) NOT NULL);
--
-- Create model InvoiceUtility
--
CREATE TABLE `contract_invoiceutility` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `contractTypeName` varchar(50) NOT NULL, `oppourtunityId` varchar(50) NOT NULL, `location` varchar(50) NULL, `invoiceStatrtDate` date NOT NULL, `invoiceEndDate` date NOT NULL, `invoiceGenrationDate` date NOT NULL, `status` varchar(2) NOT NULL, `grandTotal` double precision NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contractid_id` varchar(50) NOT NULL);
--
-- Create model KPI
--
CREATE TABLE `contract_kpi` (`kpiCode` varchar(20) NOT NULL PRIMARY KEY, `kpiName` varchar(30) NOT NULL, `status` varchar(20) NULL, `description` varchar(100) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model KPICategory
--
CREATE TABLE `contract_kpicategory` (`kpicatCode` varchar(20) NOT NULL PRIMARY KEY, `kpicatName` varchar(30) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model KPIDetail
--
CREATE TABLE `contract_kpidetail` (`kpidetid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `uom` varchar(30) NOT NULL, `targetdate` date NOT NULL, `target1` double precision NOT NULL, `typeoftarget` varchar(30) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contract_id` varchar(50) NOT NULL, `kpi_id` varchar(20) NOT NULL);
--
-- Create model KPIFrequency
--
CREATE TABLE `contract_kpifrequency` (`kpifreqid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `inputfrequency` varchar(30) NOT NULL, `outputfrequency` varchar(30) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contract_id` varchar(50) NOT NULL, `kpi_id` varchar(20) NOT NULL);
--
-- Create model RateType
--
CREATE TABLE `contract_ratetype` (`ratetypeid` integer NOT NULL PRIMARY KEY, `ratetypename` varchar(30) NOT NULL, `ratetypecode` varchar(5) NOT NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL, `contracttypeid_id` integer NULL);
--
-- Create model SkillLevel
--
CREATE TABLE `contract_skilllevel` (`skillid` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `skillname` varchar(30) NULL, `skillcode` varchar(5) NULL, `contractflag` varchar(5) NULL, `created` datetime(6) NOT NULL, `createdby` varchar(20) NOT NULL, `updated` datetime(6) NOT NULL, `updatedby` varchar(20) NOT NULL);
--
-- Create model Vertical
--
CREATE TABLE `contract_vertical` (`verticalCode` varchar(3) NOT NULL PRIMARY KEY, `verticalName` varchar(50) NULL, `verticalShortName` varchar(20) NULL);
--
-- Add field category to kpi
--
ALTER TABLE `contract_kpi` ADD COLUMN `category_id` varchar(20) NULL;
--
-- Add field skillid to detailattcapture
--
ALTER TABLE `contract_detailattcapture` ADD COLUMN `skillid_id` integer NOT NULL;
--
-- Add field contacttype to contractdetail
--
ALTER TABLE `contract_contractdetail` ADD COLUMN `contacttype_id` integer NOT NULL;
--
-- Add field contract to contractdetail
--
ALTER TABLE `contract_contractdetail` ADD COLUMN `contract_id` varchar(50) NOT NULL;
--
-- Add field designation to contractdetail
--
ALTER TABLE `contract_contractdetail` ADD COLUMN `designation_id` integer NOT NULL;
--
-- Add field ratetype to contractdetail
--
ALTER TABLE `contract_contractdetail` ADD COLUMN `ratetype_id` integer NOT NULL;
--
-- Add field skilllevel to contractdetail
--
ALTER TABLE `contract_contractdetail` ADD COLUMN `skilllevel_id` integer NOT NULL;
--
-- Add field contracttype to contract
--
ALTER TABLE `contract_contract` ADD COLUMN `contracttype_id` integer NOT NULL;
--
-- Add field customer to contract
--
ALTER TABLE `contract_contract` ADD COLUMN `customer_id` varchar(10) NULL;
--
-- Add field locationcust to contract
--
ALTER TABLE `contract_contract` ADD COLUMN `locationcust_id` integer NOT NULL;
--
-- Add field relatedcontract to contract
--
ALTER TABLE `contract_contract` ADD COLUMN `relatedcontract_id` varchar(50) NULL;
--
-- Add field contractid to capture_daily_kpi
--
ALTER TABLE `contract_capture_daily_kpi` ADD COLUMN `contractid_id` varchar(50) NOT NULL;
--
-- Add field kpiid to capture_daily_kpi
--
ALTER TABLE `contract_capture_daily_kpi` ADD COLUMN `kpiid_id` varchar(20) NOT NULL;
--
-- Add field contract to additionalcontractfield
--
ALTER TABLE `contract_additionalcontractfield` ADD COLUMN `contract_id` varchar(50) NOT NULL;
--
-- Add field invoiceid to additionalcharges
--
ALTER TABLE `contract_additionalcharges` ADD COLUMN `invoiceid_id` varchar(50) NOT NULL;
ALTER TABLE `contract_contract` ADD CONSTRAINT `contract_contract_ba_id_680ba38e_fk_account_ba_baid` FOREIGN KEY (`ba_id`) REFERENCES `account_ba` (`baid`);
ALTER TABLE `contract_contract_percentage_field` ADD CONSTRAINT `contract_contract_pe_contract_id_1d0d8afb_fk_contract_` FOREIGN KEY (`contract_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_contractdetail_reference_aadharid` ADD CONSTRAINT `contract_contractdet_contractdetailid_fk__12ce3324_fk_contract_` FOREIGN KEY (`contractdetailid_fk_id`) REFERENCES `contract_contractdetail` (`contractdetid`);
ALTER TABLE `contract_detailattcapture` ADD CONSTRAINT `contract_detailattca_contractid_id_c553d04e_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_detailattcapture` ADD CONSTRAINT `contract_detailattca_designation_id_6d2baef6_fk_contract_` FOREIGN KEY (`designation_id`) REFERENCES `contract_designation` (`designation_id`);
ALTER TABLE `contract_document` ADD CONSTRAINT `contract_document_contractid_id_26d07b4c_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_invoicedetailcapture` ADD CONSTRAINT `contract_invoicedeta_contractid_id_129e155c_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_invoiceheadermaster` ADD CONSTRAINT `contract_invoicehead_stateid_id_e792d5ac_fk_location_` FOREIGN KEY (`stateid_id`) REFERENCES `location_state` (`stateid`);
ALTER TABLE `contract_invoicemaster` ADD CONSTRAINT `contract_invoicemast_contractid_id_b404ecfe_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_invoiceutility` ADD CONSTRAINT `contract_invoiceutil_contractid_id_f3d8a939_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_kpidetail` ADD CONSTRAINT `contract_kpidetail_contract_id_b19a24ff_fk_contract_` FOREIGN KEY (`contract_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_kpidetail` ADD CONSTRAINT `contract_kpidetail_kpi_id_982b266c_fk_contract_kpi_kpiCode` FOREIGN KEY (`kpi_id`) REFERENCES `contract_kpi` (`kpiCode`);
ALTER TABLE `contract_kpifrequency` ADD CONSTRAINT `contract_kpifrequenc_contract_id_c9df40f3_fk_contract_` FOREIGN KEY (`contract_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_kpifrequency` ADD CONSTRAINT `contract_kpifrequency_kpi_id_a3376ba5_fk_contract_kpi_kpiCode` FOREIGN KEY (`kpi_id`) REFERENCES `contract_kpi` (`kpiCode`);
ALTER TABLE `contract_ratetype` ADD CONSTRAINT `contract_ratetype_contracttypeid_id_5f5ffd8d_fk_contract_` FOREIGN KEY (`contracttypeid_id`) REFERENCES `contract_contracttype` (`contracttypeid`);
ALTER TABLE `contract_kpi` ADD CONSTRAINT `contract_kpi_category_id_7300911e_fk_contract_` FOREIGN KEY (`category_id`) REFERENCES `contract_kpicategory` (`kpicatCode`);
ALTER TABLE `contract_detailattcapture` ADD CONSTRAINT `contract_detailattca_skillid_id_2a843897_fk_contract_` FOREIGN KEY (`skillid_id`) REFERENCES `contract_skilllevel` (`skillid`);
ALTER TABLE `contract_contractdetail` ADD CONSTRAINT `contract_contractdet_contacttype_id_22f723fc_fk_contract_` FOREIGN KEY (`contacttype_id`) REFERENCES `contract_contracttype` (`contracttypeid`);
ALTER TABLE `contract_contractdetail` ADD CONSTRAINT `contract_contractdet_contract_id_6d1b1bec_fk_contract_` FOREIGN KEY (`contract_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_contractdetail` ADD CONSTRAINT `contract_contractdet_designation_id_5b19a586_fk_contract_` FOREIGN KEY (`designation_id`) REFERENCES `contract_designation` (`designation_id`);
ALTER TABLE `contract_contractdetail` ADD CONSTRAINT `contract_contractdet_ratetype_id_0cc7166c_fk_contract_` FOREIGN KEY (`ratetype_id`) REFERENCES `contract_ratetype` (`ratetypeid`);
ALTER TABLE `contract_contractdetail` ADD CONSTRAINT `contract_contractdet_skilllevel_id_65046bcb_fk_contract_` FOREIGN KEY (`skilllevel_id`) REFERENCES `contract_skilllevel` (`skillid`);
ALTER TABLE `contract_contract` ADD CONSTRAINT `contract_contract_contracttype_id_15a3c7e3_fk_contract_` FOREIGN KEY (`contracttype_id`) REFERENCES `contract_contracttype` (`contracttypeid`);
ALTER TABLE `contract_contract` ADD CONSTRAINT `contract_contract_customer_id_01e9b7ca_fk_account_c` FOREIGN KEY (`customer_id`) REFERENCES `account_customer` (`custid`);
ALTER TABLE `contract_contract` ADD CONSTRAINT `contract_contract_locationcust_id_6fb1a3a9_fk_account_u` FOREIGN KEY (`locationcust_id`) REFERENCES `account_userlocationcustomer` (`ulcpkey`);
ALTER TABLE `contract_contract` ADD CONSTRAINT `contract_contract_relatedcontract_id_b1d9d0e6_fk_contract_` FOREIGN KEY (`relatedcontract_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_capture_daily_kpi` ADD CONSTRAINT `contract_capture_dai_contractid_id_bfeb8b81_fk_contract_` FOREIGN KEY (`contractid_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_capture_daily_kpi` ADD CONSTRAINT `contract_capture_dai_kpiid_id_e5e53199_fk_contract_` FOREIGN KEY (`kpiid_id`) REFERENCES `contract_kpi` (`kpiCode`);
ALTER TABLE `contract_additionalcontractfield` ADD CONSTRAINT `contract_additionalc_contract_id_89fe063a_fk_contract_` FOREIGN KEY (`contract_id`) REFERENCES `contract_contract` (`contractid`);
ALTER TABLE `contract_additionalcharges` ADD CONSTRAINT `contract_additionalc_invoiceid_id_eac53975_fk_contract_` FOREIGN KEY (`invoiceid_id`) REFERENCES `contract_invoicemaster` (`invoiceid`);
COMMIT;
