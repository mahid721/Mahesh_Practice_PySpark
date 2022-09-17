

def get_audit_insert_qry(process_id, process_name, process_status='INPROGRESS'):
    query = '''               
                insert into audit_exec_details
                (
                process_id,
                process_name ,
                process_status ,
                start_time 
                )
                Select {process_id},'{process_name}','{process_status}',getdate()
            '''.format(process_id = process_id, process_name=process_name, process_status=process_status)
    return query
def get_audit_updt_qry(process_id, process_status,error_description = ''):
    updt_query = '''
                    update audit_exec_details
                        set end_time = getdate(),
                            process_status = '{process_status}',
                            error_description = '{error_description}'
                        Where process_id = {process_id}
                            and start_time = (select  max(start_time) From audit_exec_details ) 
                            and process_status = 'INPROGRESS'
                '''.format(process_id = process_id, process_status=process_status, error_description = error_description)
    return updt_query
# get_audit_insert_qry(1,'EMP_LOAD')
