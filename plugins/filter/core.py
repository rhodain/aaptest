from ansible.errors import AnsibleFilterError

def create_multiple_dict(a, copy_count=1, start=0, field=''):
    copy_count = int(copy_count)
    start = int(start)
    r_list = [a.copy() for i in range(0, copy_count)]
    if field and field in a.keys() and isinstance(a[field], str):
        for idx, obj in enumerate(r_list):
            obj.update({field: obj[field] + f" {start+idx}"})
    return r_list

class FilterModule:
    def filters(self):
        return {
            'create_multiple_dict': create_multiple_dict
        }