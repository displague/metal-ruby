// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"strconv"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// DeviceCreateInput device create input
//
// swagger:model DeviceCreateInput
type DeviceCreateInput struct {

	// always pxe
	AlwaysPxe bool `json:"always_pxe,omitempty"`

	// billing cycle
	BillingCycle string `json:"billing_cycle,omitempty"`

	// customdata
	Customdata interface{} `json:"customdata,omitempty"`

	// description
	Description string `json:"description,omitempty"`

	// facility
	// Required: true
	Facility *string `json:"facility"`

	// features
	Features []string `json:"features"`

	// hardware reservation id
	// Example: uuid or 'next-available'
	// Format: uuid
	HardwareReservationID strfmt.UUID `json:"hardware_reservation_id,omitempty"`

	// hostname
	Hostname string `json:"hostname,omitempty"`

	// ip addresses
	IPAddresses []*DeviceCreateInputIPAddressesItems0 `json:"ip_addresses"`

	// ipxe script url
	IpxeScriptURL string `json:"ipxe_script_url,omitempty"`

	// locked
	Locked bool `json:"locked,omitempty"`

	// operating system
	// Required: true
	OperatingSystem *string `json:"operating_system"`

	// plan
	// Required: true
	Plan *string `json:"plan"`

	// private ipv4 subnet size
	PrivateIPV4SubnetSize int64 `json:"private_ipv4_subnet_size,omitempty"`

	// project ssh keys
	ProjectSSHKeys []strfmt.UUID `json:"project_ssh_keys"`

	// public ipv4 subnet size
	PublicIPV4SubnetSize int64 `json:"public_ipv4_subnet_size,omitempty"`

	// spot instance
	SpotInstance bool `json:"spot_instance,omitempty"`

	// spot price max
	SpotPriceMax float32 `json:"spot_price_max,omitempty"`

	// tags
	Tags []string `json:"tags"`

	// termination time
	// Format: date-time
	TerminationTime strfmt.DateTime `json:"termination_time,omitempty"`

	// The UUIDs of users whose SSH keys should be included on the provisioned device.
	UserSSHKeys []strfmt.UUID `json:"user_ssh_keys"`

	// userdata
	Userdata string `json:"userdata,omitempty"`
}

// Validate validates this device create input
func (m *DeviceCreateInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateFacility(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateHardwareReservationID(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateIPAddresses(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateOperatingSystem(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validatePlan(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateProjectSSHKeys(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateTerminationTime(formats); err != nil {
		res = append(res, err)
	}

	if err := m.validateUserSSHKeys(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *DeviceCreateInput) validateFacility(formats strfmt.Registry) error {

	if err := validate.Required("facility", "body", m.Facility); err != nil {
		return err
	}

	return nil
}

func (m *DeviceCreateInput) validateHardwareReservationID(formats strfmt.Registry) error {
	if swag.IsZero(m.HardwareReservationID) { // not required
		return nil
	}

	if err := validate.FormatOf("hardware_reservation_id", "body", "uuid", m.HardwareReservationID.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *DeviceCreateInput) validateIPAddresses(formats strfmt.Registry) error {
	if swag.IsZero(m.IPAddresses) { // not required
		return nil
	}

	for i := 0; i < len(m.IPAddresses); i++ {
		if swag.IsZero(m.IPAddresses[i]) { // not required
			continue
		}

		if m.IPAddresses[i] != nil {
			if err := m.IPAddresses[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("ip_addresses" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

func (m *DeviceCreateInput) validateOperatingSystem(formats strfmt.Registry) error {

	if err := validate.Required("operating_system", "body", m.OperatingSystem); err != nil {
		return err
	}

	return nil
}

func (m *DeviceCreateInput) validatePlan(formats strfmt.Registry) error {

	if err := validate.Required("plan", "body", m.Plan); err != nil {
		return err
	}

	return nil
}

func (m *DeviceCreateInput) validateProjectSSHKeys(formats strfmt.Registry) error {
	if swag.IsZero(m.ProjectSSHKeys) { // not required
		return nil
	}

	for i := 0; i < len(m.ProjectSSHKeys); i++ {

		if err := validate.FormatOf("project_ssh_keys"+"."+strconv.Itoa(i), "body", "uuid", m.ProjectSSHKeys[i].String(), formats); err != nil {
			return err
		}

	}

	return nil
}

func (m *DeviceCreateInput) validateTerminationTime(formats strfmt.Registry) error {
	if swag.IsZero(m.TerminationTime) { // not required
		return nil
	}

	if err := validate.FormatOf("termination_time", "body", "date-time", m.TerminationTime.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *DeviceCreateInput) validateUserSSHKeys(formats strfmt.Registry) error {
	if swag.IsZero(m.UserSSHKeys) { // not required
		return nil
	}

	for i := 0; i < len(m.UserSSHKeys); i++ {

		if err := validate.FormatOf("user_ssh_keys"+"."+strconv.Itoa(i), "body", "uuid", m.UserSSHKeys[i].String(), formats); err != nil {
			return err
		}

	}

	return nil
}

// ContextValidate validate this device create input based on the context it is used
func (m *DeviceCreateInput) ContextValidate(ctx context.Context, formats strfmt.Registry) error {
	var res []error

	if err := m.contextValidateIPAddresses(ctx, formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *DeviceCreateInput) contextValidateIPAddresses(ctx context.Context, formats strfmt.Registry) error {

	for i := 0; i < len(m.IPAddresses); i++ {

		if m.IPAddresses[i] != nil {
			if err := m.IPAddresses[i].ContextValidate(ctx, formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("ip_addresses" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *DeviceCreateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *DeviceCreateInput) UnmarshalBinary(b []byte) error {
	var res DeviceCreateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}

// DeviceCreateInputIPAddressesItems0 device create input IP addresses items0
//
// swagger:model DeviceCreateInputIPAddressesItems0
type DeviceCreateInputIPAddressesItems0 struct {

	// Address Family for IP Address
	// Example: 4 or 6
	AddressFamily int64 `json:"address_family,omitempty"`

	// Cidr Size for the IP Block created. Valid values depends on the operating system been provisioned.
	// Example: 28..32 for IPv4 addresses
	Cidr int64 `json:"cidr,omitempty"`

	// UUIDs of any IP reservations to use when assigning IPs
	IPReservations []string `json:"ip_reservations"`

	// Address Type for IP Address
	// Example: true or false
	Public bool `json:"public,omitempty"`
}

// Validate validates this device create input IP addresses items0
func (m *DeviceCreateInputIPAddressesItems0) Validate(formats strfmt.Registry) error {
	return nil
}

// ContextValidate validates this device create input IP addresses items0 based on context it is used
func (m *DeviceCreateInputIPAddressesItems0) ContextValidate(ctx context.Context, formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *DeviceCreateInputIPAddressesItems0) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *DeviceCreateInputIPAddressesItems0) UnmarshalBinary(b []byte) error {
	var res DeviceCreateInputIPAddressesItems0
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
