
INSERT INTO roles (id, name) VALUES
(1, 'admin'),
(2, 'manager'),
(3, 'user');


INSERT INTO business_elements (id, name, description) VALUES
(1, 'users', 'User management'),
(2, 'roles', 'Role management'),
(3, 'business_elements', 'Business elements management');


INSERT INTO access_roles_rules (
    role_id,
    element_id,
    read_permission,
    read_all_permission,
    create_permission,
    update_permission,
    update_all_permission,
    delete_permission,
    delete_all_permission
)
VALUES
(1, 1, 1, 1, 1, 1, 1, 1, 1),
(1, 2, 1, 1, 1, 1, 1, 1, 1),
(1, 3, 1, 1, 1, 1, 1, 1, 1);


INSERT INTO access_roles_rules (
    role_id,
    element_id,
    read_permission,
    read_all_permission,
    create_permission,
    update_permission,
    update_all_permission,
    delete_permission,
    delete_all_permission
)
VALUES
(2, 1, 1, 1, 1, 1, 0, 0, 0),
(2, 2, 1, 1, 0, 0, 0, 0, 0),
(2, 3, 1, 0, 0, 0, 0, 0, 0);


INSERT INTO access_roles_rules (
    role_id,
    element_id,
    read_permission,
    read_all_permission,
    create_permission,
    update_permission,
    update_all_permission,
    delete_permission,
    delete_all_permission
)
VALUES
(3, 1, 1, 0, 0, 0, 0, 0, 0),
(3, 2, 0, 0, 0, 0, 0, 0, 0),
(3, 3, 0, 0, 0, 0, 0, 0, 0);
