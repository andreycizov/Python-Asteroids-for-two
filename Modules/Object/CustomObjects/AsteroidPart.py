from Modules.Object.CustomObjects.GenericObject import GenericObjectPart


class AsteroidPart(GenericObjectPart):
        def init_custom_info (self, custom):
                if custom['Large'] == "True":
                        self.large = True
                else:
                        self.large = False
