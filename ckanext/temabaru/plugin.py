import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


# import ckanext.temabaru.cli as cli
# import ckanext.temabaru.helpers as helpers
# import ckanext.temabaru.views as views
# from ckanext.temabaru.logic import (
#     action, auth, validators
# )


class TemabaruPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "temabaru")

    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
class CustomGroupPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        return {
            'latest_group_datasets': self.latest_group_datasets
        }

    def latest_group_datasets(self, group_name, limit=3):
        context = {
            'model': toolkit.model,
            'session': toolkit.model.Session,
            'user': toolkit.g.user
        }
        data_dict = {
            'q': f'groups:{group_name}',
            'sort': 'metadata_created desc',
            'rows': limit
        }
        return toolkit.get_action('package_search')(context, data_dict)['results']
