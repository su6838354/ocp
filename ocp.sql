ALTER TABLE `app1_activities`
ADD COLUMN `status`  varchar(30) NULL DEFAULT 'pass' COMMENT 'pass 审核通过， fail 不通过，wait 待审核' AFTER `admin_id`;

