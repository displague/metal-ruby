// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"strconv"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// InstancesBatchCreateInput instances batch create input
//
// swagger:model InstancesBatchCreateInput
type InstancesBatchCreateInput struct {

	// batches
	Batches []*InstancesBatchCreateInputBatchesItems0 `json:"batches"`
}

// Validate validates this instances batch create input
func (m *InstancesBatchCreateInput) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateBatches(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *InstancesBatchCreateInput) validateBatches(formats strfmt.Registry) error {

	if swag.IsZero(m.Batches) { // not required
		return nil
	}

	for i := 0; i < len(m.Batches); i++ {
		if swag.IsZero(m.Batches[i]) { // not required
			continue
		}

		if m.Batches[i] != nil {
			if err := m.Batches[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("batches" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *InstancesBatchCreateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *InstancesBatchCreateInput) UnmarshalBinary(b []byte) error {
	var res InstancesBatchCreateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}

// InstancesBatchCreateInputBatchesItems0 instances batch create input batches items0
//
// swagger:model InstancesBatchCreateInputBatchesItems0
type InstancesBatchCreateInputBatchesItems0 struct {

	// always pxe
	AlwaysPxe bool `json:"always_pxe,omitempty"`

	// billing cycle
	BillingCycle string `json:"billing_cycle,omitempty"`

	// customdata
	Customdata interface{} `json:"customdata,omitempty"`

	// description
	Description string `json:"description,omitempty"`

	// features
	Features []string `json:"features"`

	// hostname
	Hostname string `json:"hostname,omitempty"`

	// hostnames
	Hostnames []string `json:"hostnames"`

	// ip addresses
	IPAddresses []*InstancesBatchCreateInputBatchesItems0IPAddressesItems0 `json:"ip_addresses"`

	// locked
	Locked bool `json:"locked,omitempty"`

	// operating system
	OperatingSystem string `json:"operating_system,omitempty"`

	// plan
	Plan string `json:"plan,omitempty"`

	// project ssh keys
	ProjectSSHKeys []strfmt.UUID `json:"project_ssh_keys"`

	// tags
	Tags []string `json:"tags"`

	// termination time
	// Format: date-time
	TerminationTime strfmt.DateTime `json:"termination_time,omitempty"`

	// user ssh keys
	UserSSHKeys []strfmt.UUID `json:"user_ssh_keys"`

	// userdata
	Userdata string `json:"userdata,omitempty"`
}

// Validate validates this instances batch create input batches items0
func (m *InstancesBatchCreateInputBatchesItems0) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateIPAddresses(formats); err != nil {
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

func (m *InstancesBatchCreateInputBatchesItems0) validateIPAddresses(formats strfmt.Registry) error {

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

func (m *InstancesBatchCreateInputBatchesItems0) validateProjectSSHKeys(formats strfmt.Registry) error {

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

func (m *InstancesBatchCreateInputBatchesItems0) validateTerminationTime(formats strfmt.Registry) error {

	if swag.IsZero(m.TerminationTime) { // not required
		return nil
	}

	if err := validate.FormatOf("termination_time", "body", "date-time", m.TerminationTime.String(), formats); err != nil {
		return err
	}

	return nil
}

func (m *InstancesBatchCreateInputBatchesItems0) validateUserSSHKeys(formats strfmt.Registry) error {

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

// MarshalBinary interface implementation
func (m *InstancesBatchCreateInputBatchesItems0) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *InstancesBatchCreateInputBatchesItems0) UnmarshalBinary(b []byte) error {
	var res InstancesBatchCreateInputBatchesItems0
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}

// InstancesBatchCreateInputBatchesItems0IPAddressesItems0 instances batch create input batches items0 IP addresses items0
//
// swagger:model InstancesBatchCreateInputBatchesItems0IPAddressesItems0
type InstancesBatchCreateInputBatchesItems0IPAddressesItems0 struct {

	// Address Family for IP Address
	AddressFamily int64 `json:"address_family,omitempty"`

	// Cidr Size for the IP Block created. Valid values depends on the operating system been provisioned.
	Cidr int64 `json:"cidr,omitempty"`

	// UUIDs of any IP reservations to use when assigning IPs
	IPReservations []string `json:"ip_reservations"`

	// Address Type for IP Address
	Public bool `json:"public,omitempty"`
}

// Validate validates this instances batch create input batches items0 IP addresses items0
func (m *InstancesBatchCreateInputBatchesItems0IPAddressesItems0) Validate(formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *InstancesBatchCreateInputBatchesItems0IPAddressesItems0) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *InstancesBatchCreateInputBatchesItems0IPAddressesItems0) UnmarshalBinary(b []byte) error {
	var res InstancesBatchCreateInputBatchesItems0IPAddressesItems0
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
