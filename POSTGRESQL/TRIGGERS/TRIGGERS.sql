drop function tg_testDelete;

create function tg_test() returns Trigger
as
$$
begin
	
	insert into calculation_master_algorithms_h(
		algorithm_saratoga_id, 
		algorithm_name, 
		algorithm_description, 
		algorithm_audit_add_timestamp, 
		algorithm_audit_add_user, 
		algorithm_audit_status, 
		algorithm_audit_status_timestamp, 
		algorithm_audit_status_user
	)
	values(
		new.algorithm_saratoga_id, 
		new.algorithm_name, 
		new.algorithm_description,
		new.algorithm_audit_add_timestamp,
		new.algorithm_audit_add_user,
		new.algorithm_audit_status,
		new.algorithm_audit_status_timestamp, 
		new.algorithm_audit_status_user
	);
	
	return new;
end
$$ 
LANGUAGE plpgsql;

create function tg_testDelete() returns Trigger
as
$$
begin
	
	insert into calculation_master_algorithms_h(
		algorithm_saratoga_id, 
		algorithm_name, 
		algorithm_description, 
		algorithm_audit_add_timestamp, 
		algorithm_audit_add_user, 
		algorithm_audit_status, 
		algorithm_audit_status_timestamp, 
		algorithm_audit_status_user
	)
	values(
		old.algorithm_saratoga_id, 
		old.algorithm_name, 
		old.algorithm_description,
		old.algorithm_audit_add_timestamp,
		old.algorithm_audit_add_user,
		'D',
		current_timestamp,
		old.algorithm_audit_status_user
	);
	
	return new;
end
$$ 
LANGUAGE plpgsql;

-- PARA UPDATE
create trigger tg_update before update on calculation_master_algorithms
for each row 
execute procedure tg_test() ;

-- PARA INSERT
create trigger tg_create before insert on calculation_master_algorithms
for each row 
execute procedure tg_test() ;

-- PARA DELETE
create trigger tg_delete after delete on calculation_master_algorithms
for each row 
execute procedure tg_testDelete() ;



INSERT INTO public.calculation_master_algorithms_h
(algorithm_saratoga_id, algorithm_name, algorithm_description, algorithm_audit_add_timestamp, algorithm_audit_add_user, algorithm_audit_status, algorithm_audit_status_timestamp, algorithm_audit_status_user)
VALUES('', '', '', '', '', '', '', '');

