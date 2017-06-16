# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.preview.wireless.sim.usage import UsageList


class SimList(ListResource):

    def __init__(self, version):
        """
        Initialize the SimList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.wireless.sim.SimList
        :rtype: twilio.rest.preview.wireless.sim.SimList
        """
        super(SimList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Sims'.format(**self._solution)

    def stream(self, status=values.unset, iccid=values.unset,
               rate_plan=values.unset, e_id=values.unset,
               sim_registration_code=values.unset, limit=None, page_size=None):
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode status: The status
        :param unicode iccid: The iccid
        :param unicode rate_plan: The rate_plan
        :param unicode e_id: The e_id
        :param unicode sim_registration_code: The sim_registration_code
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.sim.SimInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, status=values.unset, iccid=values.unset, rate_plan=values.unset,
             e_id=values.unset, sim_registration_code=values.unset, limit=None,
             page_size=None):
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode status: The status
        :param unicode iccid: The iccid
        :param unicode rate_plan: The rate_plan
        :param unicode e_id: The e_id
        :param unicode sim_registration_code: The sim_registration_code
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.wireless.sim.SimInstance]
        """
        return list(self.stream(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, iccid=values.unset, rate_plan=values.unset,
             e_id=values.unset, sim_registration_code=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately

        :param unicode status: The status
        :param unicode iccid: The iccid
        :param unicode rate_plan: The rate_plan
        :param unicode e_id: The e_id
        :param unicode sim_registration_code: The sim_registration_code
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimPage
        """
        params = values.of({
            'Status': status,
            'Iccid': iccid,
            'RatePlan': rate_plan,
            'EId': e_id,
            'SimRegistrationCode': sim_registration_code,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SimPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SimPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SimContext

        :param sid: The sid

        :returns: twilio.rest.preview.wireless.sim.SimContext
        :rtype: twilio.rest.preview.wireless.sim.SimContext
        """
        return SimContext(
            self._version,
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a SimContext

        :param sid: The sid

        :returns: twilio.rest.preview.wireless.sim.SimContext
        :rtype: twilio.rest.preview.wireless.sim.SimContext
        """
        return SimContext(
            self._version,
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.SimList>'


class SimPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SimPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.wireless.sim.SimPage
        :rtype: twilio.rest.preview.wireless.sim.SimPage
        """
        super(SimPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SimInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.wireless.sim.SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimInstance
        """
        return SimInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Wireless.SimPage>'


class SimContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the SimContext

        :param Version version: Version that contains the resource
        :param sid: The sid

        :returns: twilio.rest.preview.wireless.sim.SimContext
        :rtype: twilio.rest.preview.wireless.sim.SimContext
        """
        super(SimContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'sid': sid,
        }
        self._uri = '/Sims/{sid}'.format(**self._solution)

        # Dependents
        self._usage = None

    def fetch(self):
        """
        Fetch a SimInstance

        :returns: Fetched SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    def update(self, unique_name=values.unset, callback_method=values.unset,
               callback_url=values.unset, friendly_name=values.unset,
               rate_plan=values.unset, status=values.unset,
               commands_callback_method=values.unset,
               commands_callback_url=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, voice_fallback_method=values.unset,
               voice_fallback_url=values.unset, voice_method=values.unset,
               voice_url=values.unset):
        """
        Update the SimInstance

        :param unicode unique_name: The unique_name
        :param unicode callback_method: The callback_method
        :param unicode callback_url: The callback_url
        :param unicode friendly_name: The friendly_name
        :param unicode rate_plan: The rate_plan
        :param unicode status: The status
        :param unicode commands_callback_method: The commands_callback_method
        :param unicode commands_callback_url: The commands_callback_url
        :param unicode sms_fallback_method: The sms_fallback_method
        :param unicode sms_fallback_url: The sms_fallback_url
        :param unicode sms_method: The sms_method
        :param unicode sms_url: The sms_url
        :param unicode voice_fallback_method: The voice_fallback_method
        :param unicode voice_fallback_url: The voice_fallback_url
        :param unicode voice_method: The voice_method
        :param unicode voice_url: The voice_url

        :returns: Updated SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'FriendlyName': friendly_name,
            'RatePlan': rate_plan,
            'Status': status,
            'CommandsCallbackMethod': commands_callback_method,
            'CommandsCallbackUrl': commands_callback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    @property
    def usage(self):
        """
        Access the usage

        :returns: twilio.rest.preview.wireless.sim.usage.UsageList
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageList
        """
        if self._usage is None:
            self._usage = UsageList(
                self._version,
                sim_sid=self._solution['sid'],
            )
        return self._usage

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.SimContext {}>'.format(context)


class SimInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the SimInstance

        :returns: twilio.rest.preview.wireless.sim.SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimInstance
        """
        super(SimInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'rate_plan_sid': payload['rate_plan_sid'],
            'friendly_name': payload['friendly_name'],
            'iccid': payload['iccid'],
            'e_id': payload['e_id'],
            'status': payload['status'],
            'commands_callback_url': payload['commands_callback_url'],
            'commands_callback_method': payload['commands_callback_method'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_url': payload['sms_url'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimContext
        """
        if self._context is None:
            self._context = SimContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique_name
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def rate_plan_sid(self):
        """
        :returns: The rate_plan_sid
        :rtype: unicode
        """
        return self._properties['rate_plan_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def iccid(self):
        """
        :returns: The iccid
        :rtype: unicode
        """
        return self._properties['iccid']

    @property
    def e_id(self):
        """
        :returns: The e_id
        :rtype: unicode
        """
        return self._properties['e_id']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def commands_callback_url(self):
        """
        :returns: The commands_callback_url
        :rtype: unicode
        """
        return self._properties['commands_callback_url']

    @property
    def commands_callback_method(self):
        """
        :returns: The commands_callback_method
        :rtype: unicode
        """
        return self._properties['commands_callback_method']

    @property
    def sms_fallback_method(self):
        """
        :returns: The sms_fallback_method
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The sms_method
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The sms_url
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def voice_fallback_method(self):
        """
        :returns: The voice_fallback_method
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The voice_method
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The voice_url
        :rtype: unicode
        """
        return self._properties['voice_url']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a SimInstance

        :returns: Fetched SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset, callback_method=values.unset,
               callback_url=values.unset, friendly_name=values.unset,
               rate_plan=values.unset, status=values.unset,
               commands_callback_method=values.unset,
               commands_callback_url=values.unset, sms_fallback_method=values.unset,
               sms_fallback_url=values.unset, sms_method=values.unset,
               sms_url=values.unset, voice_fallback_method=values.unset,
               voice_fallback_url=values.unset, voice_method=values.unset,
               voice_url=values.unset):
        """
        Update the SimInstance

        :param unicode unique_name: The unique_name
        :param unicode callback_method: The callback_method
        :param unicode callback_url: The callback_url
        :param unicode friendly_name: The friendly_name
        :param unicode rate_plan: The rate_plan
        :param unicode status: The status
        :param unicode commands_callback_method: The commands_callback_method
        :param unicode commands_callback_url: The commands_callback_url
        :param unicode sms_fallback_method: The sms_fallback_method
        :param unicode sms_fallback_url: The sms_fallback_url
        :param unicode sms_method: The sms_method
        :param unicode sms_url: The sms_url
        :param unicode voice_fallback_method: The voice_fallback_method
        :param unicode voice_fallback_url: The voice_fallback_url
        :param unicode voice_method: The voice_method
        :param unicode voice_url: The voice_url

        :returns: Updated SimInstance
        :rtype: twilio.rest.preview.wireless.sim.SimInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            callback_method=callback_method,
            callback_url=callback_url,
            friendly_name=friendly_name,
            rate_plan=rate_plan,
            status=status,
            commands_callback_method=commands_callback_method,
            commands_callback_url=commands_callback_url,
            sms_fallback_method=sms_fallback_method,
            sms_fallback_url=sms_fallback_url,
            sms_method=sms_method,
            sms_url=sms_url,
            voice_fallback_method=voice_fallback_method,
            voice_fallback_url=voice_fallback_url,
            voice_method=voice_method,
            voice_url=voice_url,
        )

    @property
    def usage(self):
        """
        Access the usage

        :returns: twilio.rest.preview.wireless.sim.usage.UsageList
        :rtype: twilio.rest.preview.wireless.sim.usage.UsageList
        """
        return self._proxy.usage

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.SimInstance {}>'.format(context)
