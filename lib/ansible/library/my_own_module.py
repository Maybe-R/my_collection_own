from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True),
        force_change=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        path_written='',
        content_written=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    path = module.params['path']
    content = module.params['content']
    force_change = module.params['force_change']

    result['path_written'] = path
    result['content_written'] = content

    current_content = ""
    file_exists = os.path.exists(path)

    if file_exists:
        with open(path, 'r') as f:
            current_content = f.read()

    if current_content != content or not file_exists or force_change:
        try:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Failed to write file {path}: {e}", **result)
    else:
        result['changed'] = False

    module.exit_json(**result)

if __name__ == '__main__':
    run_module()
